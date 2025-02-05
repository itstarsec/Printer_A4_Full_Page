# Hướng dẫn sử dụng Script In Ảnh A4 Nằm Ngang

Script Python này cho phép bạn kết nối đến máy in qua địa chỉ IP và in một file hình ảnh với kích thước A4 nằm ngang. Sau đây là hướng dẫn chi tiết để bạn có thể sử dụng script này một cách dễ dàng và hiệu quả.

## Yêu cầu

- Python 3.x
- Các thư viện Python sau:
  - Pillow
  - pywin32

## Cài đặt các thư viện cần thiết

Trước tiên, hãy cài đặt các thư viện cần thiết bằng cách sử dụng pip. Mở terminal hoặc command prompt và chạy lệnh sau:

```bash
pip install pillow pywin32
```
## Cấu hình máy in
### Thêm máy in vào hệ thống:

``` Vào Settings > Devices > Printers & scanners trên Windows.
Nhấn vào Add a printer or scanner.
Nhập địa chỉ IP của máy in (192.168.10.200) trong quá trình cài đặt và nhấn Next.
Đặt tên cho máy in và hoàn tất quá trình cài đặt.
Ghi lại tên máy in:
```
### Tên máy in mà bạn đã cài đặt sẽ được sử dụng trong script.
## Sử dụng script
### Chỉnh sửa script:

Mở file script Python (ví dụ: printfileA4.py) trong một trình soạn thảo văn bản.
Thay thế "Tên máy in của bạn" trong mã bằng tên máy in thực tế mà bạn đã cài đặt.
### Chạy script:

Đảm bảo rằng file hình ảnh bạn muốn in đã có sẵn theo đường dẫn đã chỉ định:

C:\tmp\test.jpg
Mở terminal hoặc command prompt, điều hướng đến thư mục chứa file script và chạy lệnh:
```
python printfileA4.py
```
Chúc thành công!
Hy vọng rằng bạn sẽ thành công trong việc sử dụng script này để in hình ảnh. Nếu bạn gặp phải bất kỳ vấn đề nào, hãy kiểm tra lại các bước trên hoặc nhắn vào mục issues nhé..

Cảm ơn bạn đã sử dụng script này!
