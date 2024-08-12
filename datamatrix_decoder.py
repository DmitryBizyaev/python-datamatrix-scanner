from pylibdmtx.pylibdmtx import decode
from PIL import Image


# Функция на вход получает путь к изображению и
# возвращает декодированные данные DataMatrix кодов
# расположенных на данном изображении.
def decode_datamatrix_code(image_path):

	decoded = decode(Image.open(image_path))

	return [d.data for d in decoded]