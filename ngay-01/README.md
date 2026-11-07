# Ngày 1 · Python khác gì ngôn ngữ bạn biết

> Python AI 80 ngày · 1. Python cho người đã biết code · video 1 phút 33 giây

## Bạn học gì

Python khác gì ngôn ngữ bạn biết: thụt lề, kiểu động, f-string

## Bài học

_Đi theo đúng thứ tự video. Lời giảng là lời đọc trong video; code và kết quả là bản máy đã chạy thật._

### NGÀY 1 · THỤT LỀ, KIỂU ĐỘNG, F-STRING

Giá trà sữa lưu thành chữ rồi nhân ba, in ra gì?

File `buoc_1.py` — chạy: `python buoc_1.py`

```python
gia = 35000
gia = "35k"
print(gia * 3)
```

**Đoán trước khi chạy — Giá dạng chữ nhân ba — in ra gì?**

- A. `105000`
- B. `35k35k35k`
- C. `Lỗi khi chạy`

Kết quả (máy đã chạy thật):

```text
35k35k35k
```

Đáp án đúng: **B**.

Chữ lặp ba lần, không lỗi — mà đơn web gửi về toàn dạng chữ. Vậy sao trừ năm nghìn lại bị từ chối?

### Ý chính — CUỐI KHÓA LÀM ĐƯỢC — 80 ngày làm được gì

Đó mới là ngày một trên tám mươi. Qua bảng dữ liệu, học máy, mạng nơ-ron, tới ngày cuối tự làm trợ lý homestay trả lời có trích nguồn. F-string hôm nay là viên gạch đầu: ghép câu hỏi với tài liệu.

- **pandas, NumPy** — bảng dữ liệu, mảng số
- **scikit-learn** — huấn luyện, chấm điểm mô hình
- **PyTorch** — tự viết vòng huấn luyện
- **API LLM** — dùng tool, RAG có trích nguồn

Ghi nhớ nhanh: 80 ngày học đều · mỗi ngày 1 video code chạy thật · dự án cuối trợ lý homestay

### KIỂU ĐỘNG, KIỂU MẠNH — Trừ số khỏi chữ?

Quay lại giá chữ, áp luật từ ba ly giảm năm nghìn.

File `loi_1.py` — chạy: `python loi_1.py`

```python
gia = "35k"
so_ly = 3
if so_ly >= 3:
    gia = gia - 5000
print(gia * so_ly)
```

Lỗi máy báo (cố ý; rút gọn như trên video):

```text
TypeError: unsupported operand type(s) for
-: 'str' and 'int' (dòng 4)
```

Tới phép trừ thì dừng: lỗi kiểu TypeError. Kiểu động nên đổi sang chữ được, nhưng kiểu mạnh nên không tự đổi lại số.

### THỤT LỀ — Giá về số, khối nhờ thụt lề

File `buoc_2.py` — chạy: `python buoc_2.py`

```python
gia = 35000
so_ly = 3
if so_ly >= 3:
    gia = gia - 5000
print(gia * so_ly)
```

Kết quả (máy đã chạy thật):

```text
90000
```

Vậy trả giá về số, không khai báo kiểu: chín mươi nghìn. Cùng luật ai cũng biết, chỉ viết gọn: không ngoặc nhọn, không chấm phẩy. Lùi dòng một nấc nghĩa là dòng đó nằm trong luật giảm giá.

### F-STRING — In hóa đơn bằng f-string

Giờ in hóa đơn bằng f-string: biểu thức đặt thẳng giữa câu.

File `buoc_3.py` — chạy: `python buoc_3.py`

```python
gia = 35000
so_ly = 3
if so_ly >= 3:
    gia = gia - 5000
print(f"{so_ly} ly: {gia * so_ly:,}đ")
print(f"{gia=}")
```

Kết quả (máy đã chạy thật):

```text
3 ly: 90,000đ
gia=30000
```

Dấu phẩy sau nó chèn dấu ngăn nghìn. Mẹo dân code: dấu bằng sau tên biến in cả tên lẫn giá trị.

### Ý chính — TRỌNG TÂM — Khác C, Java ở bốn điểm

Vậy gom lại: hai chấm mở khối, thụt đều, quy ước bốn dấu cách. Biến gán lại kiểu khác được, lỗi kiểu chỉ lộ khi chạy.

- **dấu :** — mở khối if, for, def
- **thụt lề** — thay {}, quy ước 4 dấu cách
- **kiểu động** — không khai báo, gán lại kiểu khác
- **kiểu mạnh** — không tự đổi kiểu

Ghi nhớ nhanh: thụt lề = khối lệnh · lỗi kiểu lộ khi chạy · f-string {gia * so_ly:,}

### LỖI HAY GẶP — Thiếu một dấu hai chấm

Nhưng quên dấu hai chấm cuối điều kiện thì sao?

File `loi_2.py` — chạy: `python loi_2.py`

```python
gia = 35000
so_ly = 3
if so_ly >= 3
    gia = gia - 5000
print(gia * so_ly)
```

**Đoán trước khi chạy — Thiếu một dấu «:» — in ra gì?**

- A. `90000`
- B. `105000`
- C. `Lỗi biên dịch`

Lỗi máy báo (cố ý; rút gọn như trên video):

```text
Dòng 3: SyntaxError: expected ':'
```

Đáp án đúng: **C**.

Không dòng nào chạy: lỗi cú pháp SyntaxError, chỉ đúng dòng thiếu. Thêm dấu là chạy; trộn tab với dấu cách cũng bị chặn vậy.

## Tóm lại

Tóm lại: Python dùng thụt lề, kiểu động mà mạnh, in bằng f-string. Giờ bạn biết vì sao chữ nhân ba êm, còn trừ thì lỗi.

## Câu đố hôm nay

In ra gì? Đoán trước, rồi chạy thử. Đáp án ở Ngày 2.

```python
gia = "5000"
print(f"{gia * 2}đ")
```

## Bài tập

Tổng dưới 100.000đ thì cộng ship 15.000đ, in tổng mới có dấu phẩy ngăn nghìn.
