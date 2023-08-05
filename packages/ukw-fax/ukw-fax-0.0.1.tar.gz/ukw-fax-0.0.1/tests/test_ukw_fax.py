from ukw_fax.cli import main
from pathlib import Path
from ukw_fax import export_messages


def test_main():
    assert main([]) == 0


# def test_export_fax():
#     path_attachments = Path("test/attachments")
#     path_export = Path("test/export")

#     export_messages(
#         path_attachments=path_attachments,
#         path_export=path_export,
#         image_as_jpg=False
#     )

#     export_number_folder = path_attachments.joinpath("+49123")
#     export_timestamp_folder = export_number_folder.joinpath()

#     assert export_number_folder.exists()
#     assert export_timestamp_folder.exists()  # Insert Timestamp like 210518-111510
#     assert export_timestamp_folder.joinpath().exists()  # 2141928_FAX_210510-112310.tif
#     assert export_timestamp_folder.joinpath("mail.json").exists()
#     assert export_timestamp_folder.joinpath("ocr_result.txt").exists()
