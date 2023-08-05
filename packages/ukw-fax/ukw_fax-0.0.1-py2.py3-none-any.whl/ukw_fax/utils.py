import pathlib
import json
import os
import pytesseract
from PIL import Image
from tqdm.auto import tqdm
import mailparser


def export_messages(
    path_attachments: pathlib.Path,
    path_export: pathlib.Path,
    image_as_jpg: bool = False,
):
    """
    Method to read all .msg files in the given folder.
    Returns list of msg objects.

    Parameters:
    path_attachments - pathlib.Path
        Path to folder containing all messages to be read.
    path_export - pathlib.Path
        Path to folder to save exports in
    path_tmp - pathlib.Path
        Path to folder used to temporarily store objects.
    path_tesseract - pathlib.path
        Path to local tesseract.exe
    image_as_jpg - bool
        If true, image is additionally exported as .jpg file, otherwise it is just exported as .tif file
    """
    assert path_attachments.exists()
    assert path_export.exists()

    ocr_result_name = "ocr_result.txt"

    filenames = [fn for fn in path_attachments.iterdir()]
    assert len(filenames) > 0

    for filename in tqdm(filenames):
        msg = mailparser.parse_from_file_msg(filename)
        msg_dict = msg.mail_partial
        assert len(msg_dict["from"][0]) == 2

        # get fax number of sender
        number = msg_dict["from"][0][1].split("/")[1].split('"')[0]
        # set path
        path_praxis = path_export.joinpath(number)
        # create folder if it doesnt exist
        if not path_praxis.exists():
            os.mkdir(path_praxis)
        name_tif = msg_dict["attachments"][0]["filename"]
        timestamp = name_tif.split("FAX_")[1].split(".")[0]
        # save final msg
        msg_export_path = path_praxis.joinpath(timestamp)
        i = 0
        _name = msg_export_path.name
        while msg_export_path.exists() is True:
            msg_export_path = msg_export_path.with_name(f"{_name}_({i})")
            i = +1

        os.mkdir(msg_export_path)
        # save json
        del msg_dict["attachments"]
        del msg_dict["date"]

        with open(msg_export_path.joinpath("mail.json"), "w") as f:
            json.dump(msg_dict, f)
        # write_msg
        msg.write_attachments(msg_export_path)

        # read image and run tesseract
        path_to_current_tif = msg_export_path.joinpath(name_tif)
        img = Image.open(path_to_current_tif)
        if image_as_jpg:
            img.save(path_to_current_tif.with_suffix(".jpg"))
        msg_txt = pytesseract.image_to_string(img, lang="deu")
        # save text
        with open(msg_export_path.joinpath(ocr_result_name), "w", encoding="utf8") as f:
            f.write(msg_txt)
