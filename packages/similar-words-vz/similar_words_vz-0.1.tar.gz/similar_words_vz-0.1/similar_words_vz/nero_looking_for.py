import pandas as pd
import torch
import numpy as np


def main(text, book, batch_size=64, model_checkpoint='sergiyvl/model_65000_20ep'):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # if device == 'cpu':
    #     print('cpu')
    # else:
    #     n_gpu = torch.cuda.device_count()
    #     print(torch.cuda.get_device_name(0))
    adress_book = 'books/mt_gold_65875.csv'
    csv_book = pd.read_csv(adress_book)
    book = [sent[1] for sent in csv_book.values]

    model, tokenizer = load_model(model_checkpoint)

    result, key_key_tokens, obraz, obraz_tokenize = find_words_in_book(device, book, tokenizer, model, batch_size)

    book_helpfull = ["Божественную явления Твоего доброту пророк провидя, и снизхождению ужасаяся воплощения Христе, предвозгласи: от юга приидет Господь очищение мирови даруяй."]

    result_list = list(result)
    result_list.sort(key=lambda x: sum(x[1]), reverse=True)
    i = 0
    print(result.shape)
    for el in result_list[:600]:
        i += 1
        array = el[1] > 1
        # print(el[1][array], end=" ")
        book_helpfull.append(book[int(el[0, 0])])
        # print(i, book_helpfull[int(el[0, 0])])
        if i <= 100:
            print(i, book[int(el[0, 0])])
    
    # Собираем два массива с ключевыми буквосочетаниями и без
    texts_with_key_key = []
    texts_without_key_key = []
    for text in book_helpfull:
        key_key_exist = True
        for key_key in key_key_tokens:
            if key_key.upper() not in text.upper():
                key_key_exist = False
        if key_key_exist:
            texts_with_key_key.append(text)
        else:
            texts_without_key_key.append(text)
        
    i = 0
    for text in texts_with_key_key:
    i += 1
    print(i, text)


def load_model(model_checkpoint=None):
    # подгружаем нужную модель
    if model_checkpoint == None:
        model_checkpoint = 'sergiyvl/model_65000_20ep'

    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

    from transformers import AutoModelForMaskedLM
    model = AutoModelForMaskedLM.from_pretrained(model_checkpoint)

    return model, tokenizer



def find_words_in_book(device, book, tokenizer, model, batch_size=64):
    """
    Седьмая вариация. Нормализация по вектору образа. В сравнение идут все вектора кроме первого, точки и последнего.
    Ключевые токены возводятся в степень. Ключевые токены, образующие слова, зависят друг от друга. (otn = batch_max[i][ind-1]/batch_max[i][ind]). 
    Есть возможность ввести ключевые буквосочетания.
    Добавлена грубая реакция на сочетание ключевых токенов. (коэфициент - сумма токенов > 200)
    """
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # ВВОДИМ ОБРАЗ И ВЫБИРАЕМ КЛЮЧЕВЫЕ ТОКЕНЫ И БУКВОСОЧЕТАНИЯ
    obraz = input("Введите образ: ")

    obraz_tokenize = tokenizer.tokenize(obraz)

    i = 0
    for token in obraz_tokenize:
        i += 1
        print("(", i,", "+token+")", end="  ", sep="")
        if i%10 == 0:
            print()
    order = [int(i) for i in input("\nВведите через пробел номера ключевых токенов: ").split()]

    relevant = [(1 if i+1 not in order else 1.5) for i in range(len(obraz_tokenize))]

    key_key_tokens = [i for i in input("Введите буквосочетания, без которых в тексте точно нет образа (одно или несколько, если несколько - через пробел):").split()]


    # ТОКЕНИЗИРУЕМ ТЕКСТ И НОРМАЛИЗУЕМ СЛОВА
    batch_size=64
    text_tokenized = tokenizer(text, return_tensors='pt').to(device)
    text_throw_model = model(
                            **text_tokenized,
                            output_hidden_states=True
                        ).hidden_states[:][-1]


    words = text_throw_model[0][1:-1].reshape(1, -1, 768)

    normalization_token = []
    for word in obraz_tokenize:
        token = tokenizer(word+'.', return_tensors='pt').to(device)
        token_1 = model(
            **token,
            output_hidden_states=True  
        ).hidden_states[:][-1]
        token_2 = torch.transpose(token_1, 1, 2)
        koef = 40/(token_1 @ token_2)[0, 1, 1].detach().cpu().numpy()
        normalization_token.append(koef)

    normalization_word = []
    # normilization = 40/(words@torch.transpose(words, 1, 2)) ЧТО ПО СУТИ ВНИЗУ ПРОИСХОДИТ
    for word in words[0]:
        word_transpose = torch.transpose(word.reshape(1, -1), 0, 1)
        koef = 40/(word.reshape(1, -1) @ word_transpose)[0, 0].detach().cpu().numpy()
        normalization_word.append(koef)

    for i in range(len(normalization_word)):
        print(obraz_tokenize[i], normalization_token[i], normalization_word[i])
        
    # ИЩЕМ ПАРЫ КЛЮЧЕВЫХ ТОКЕНОВ, КОТОРЫЕ ОБРАЗУЮТ СЛОВА, ЧТОБЫ В БУДУЩЕМ НОРМАЛИЗОВАТЬ ОТНОСИТЕЛЬНО ИХ СОВМЕСТНОЙ ВСТРЕЧАЕМОСТИ
    pairs_second = []
    for i in range(len(relevant)):
        if relevant[i] > 1:
            if obraz_tokenize[i][:2] == "##":
                if relevant[i-1] > 1:
                    pairs_second.append(i)
    print(pairs_second)

    # ПРОГОНЯЕМ ЧЕРЕЗ МОДЕЛЬ И СОХРАНЯЕМ В result ИТОГИ
    result = np.zeros((len(book), 2, len(relevant)))

    for start_index in range(0, len(book), batch_size):
        batch = book[start_index:start_index+batch_size]

        batch = tokenizer(batch, return_tensors='pt',truncation=True, padding=True, max_length=45).to(device)

        batch = model(
        **batch,
        output_hidden_states=True
        ).hidden_states[:][-1]

    #  КАЖДЫЙ БАТЧ ПЕРЕМНОЖАЕТСЯ С МАТРИЦЕЙ ТЕКСТА И ЛУЧШИЕ РЕЗУЛЬТАТЫ ОСТАВЛЯЮТСЯ
        batch = torch.transpose(batch, 1, 2)
        
        batch = (words @ batch).detach().cpu().numpy()
        batch = batch[:, :, 1:-1]

        batch_max = np.max(batch, axis=2)
        for i in np.arange(batch_size):
            if start_index+i<len(book):
                result[start_index+i][0][0] = start_index+i
                # print(relevant, batch_max[i])
                for ind in pairs_second:
                    otn = batch_max[i][ind-1]/batch_max[i][ind]
                    normalization_word[ind-1] *= (otn if otn < 1 else 1/otn)
                    result[start_index+i][1] = (batch_max[i]*normalization_token)**relevant # СМОТРИ КАКАЯ НОРМАЛИЗАЦИЯ

    return result, key_key_tokens, obraz, obraz_tokenize