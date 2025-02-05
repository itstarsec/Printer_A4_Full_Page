import win32print
import win32ui
from PIL import Image, ImageWin

# Tên máy in đã được cài đặt trong hệ thống
printer_name = "Tên máy in của bạn"  # Thay thế bằng tên máy in thực tế của bạn

# Đường dẫn của file hình ảnh
image_path = r"C:\tmp\test.jpg"

# Mở hình ảnh
image = Image.open(image_path)

# Chuyển đổi kích thước hình ảnh để phù hợp với kích thước A4 nằm ngang
# Kích thước A4 nằm ngang là 29.7 cm x 21 cm (297 mm x 210 mm)
# Tỉ lệ DPI (dots per inch), thường là 300 cho in ấn chất lượng cao
dpi = 300
a4_width = int(11.69 * dpi)  # 11.69 inch
a4_height = int(8.27 * dpi)   # 8.27 inch
image = image.resize((a4_width, a4_height), Image.LANCZOS)  # Sử dụng Image.LANCZOS

# Khởi tạo máy in
hprinter = win32print.OpenPrinter(printer_name)
try:
    # Bắt đầu một bản in
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)  # Tạo kết nối đến máy in
    hdc.StartDoc("Print Image")
    hdc.StartPage()

    # In hình ảnh
    dib = ImageWin.Dib(image)
    dib.draw(hdc.GetHandleOutput(), (0, 0, a4_width, a4_height))

    # Kết thúc bản in
    hdc.EndPage()
    hdc.EndDoc()
finally:
    win32print.ClosePrinter(hprinter)