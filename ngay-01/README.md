# Ngày 1 · Python khác gì ngôn ngữ bạn biết

Python AI 80 ngày · 1. Python cho người đã biết code

## Bạn học gì

Python khác gì ngôn ngữ bạn biết: thụt lề, kiểu động, f-string

## Code trong video

### NGÀY 1 · THỤT LỀ, KIỂU ĐỘNG, F-STRING

File `buoc_1.py` — chạy: `python buoc_1.py`

```python
gia = 35000
gia = "35k"
print(gia * 3)
```

Kết quả (máy đã chạy thật):

```text
35k35k35k
```

### KIỂU ĐỘNG, KIỂU MẠNH — Trừ số khỏi chữ?

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

### F-STRING — In hóa đơn bằng f-string

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

### LỖI HAY GẶP — Thiếu một dấu hai chấm

File `loi_2.py` — chạy: `python loi_2.py`

```python
gia = 35000
so_ly = 3
if so_ly >= 3
    gia = gia - 5000
print(gia * so_ly)
```

Lỗi máy báo (cố ý; rút gọn như trên video):

```text
Dòng 3: SyntaxError: expected ':'
```

## Câu đố hôm nay

In ra gì? Đoán trước, rồi chạy thử. Đáp án ở Ngày 2.

```python
gia = "5000"
print(f"{gia * 2}đ")
```

## Bài tập

Tổng dưới 100.000đ thì cộng ship 15.000đ, in tổng mới có dấu phẩy ngăn nghìn.
