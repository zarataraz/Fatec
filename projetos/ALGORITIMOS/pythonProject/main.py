import os
import requests

url_base = "https://siga.cps.sp.gov.br/image//"
output_directory = "imagens"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

    for i in range(1,10):
        image_url = f"{url_base}{i}.jpg"
        response = requests.get(image_url)

        if response.status_code ==200:
            image_path = os.path.join(output_directory, f"image_{i}.jpg")
            with open(image_path, "wb") as f:
                f.write(response.content)
                print(f"imagem {i} baixada com sucesso.")
        else:
                print(f"falaha ao baixar a imagem {i}")