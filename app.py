from flask import Flask, render_template, redirect, request
import datamatrix_decoder


app = Flask(__name__)


# Отрисовка начальной страницы
@app.route("/", methods=['GET'])
def start():
    output_text = "Загрузите изображение с DataMatrix кодом для декодировки!"

    return render_template('index.html', output_text=output_text)


# Отрисовка страницы с результатами декодирования
@app.route("/upload_file", methods=['POST'])
def upload_file():

    # Получение информации об изображении и запись ее в файл
    image_data = request.files['file_data'].read()

    file_name = "received_image.png"
    with open(file_name, 'wb') as file:
        file.write(image_data)

    # Декодирование
    decoded = datamatrix_decoder.decode_datamatrix_code(file_name)

    # Обработка строки с результатами
    if decoded != []:
        if len(decoded) > 1:
            decoded_text = "Информация, полученная из DataMagtrix кодов:\n"

            for idx, d in enumerate(decoded):
                decoded_text += f'\n{idx + 1}. {d.decode("utf-8")}'

        else:
             decoded_text = f'Информация, полученная из DataMagtrix кода:\n{decoded[0].decode("utf-8")}'

    else:
        decoded_text = "На данном изображении не было обнаружено DataMatrix кодов"

    return render_template('index.html', output_text=decoded_text)