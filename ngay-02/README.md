# Ngày 2 · Số trong Python

Python AI 80 ngày · 1. Python cho người đã biết code

## Bạn học gì

Số trong Python: /, //, %, int không tràn, round(2.5) = 2

## Code trong video

### NGÀY 2 · SỐ TRONG PYTHON

File `buoc_1.py` — chạy: `python buoc_1.py`

```python
don = 17
shipper = 5
print(don / shipper)
```

Kết quả (máy đã chạy thật):

```text
3.4
```

### THÊM MỘT GẠCH — Chia lấy phần nguyên

File `buoc_2.py` — chạy: `python buoc_2.py`

```python
don = 17
shipper = 5
print(don // shipper)
```

Kết quả (máy đã chạy thật):

```text
3
```

### PHẦN DƯ VÀ SỐ ÂM — Dư mấy đơn? Số âm thì sao?

File `buoc_3.py` — chạy: `python buoc_3.py`

```python
don = 17
shipper = 5
print(don // shipper)
print(don % shipper)
print(-don // shipper)
```

Kết quả (máy đã chạy thật):

```text
3
2
-4
```

### BẪY LÀM TRÒN — round(2.5) ra mấy?

File `buoc_4.py` — chạy: `python buoc_4.py`

```python
so_km = 2.5
print(round(so_km), round(so_km + 1))
```

Kết quả (máy đã chạy thật):

```text
2 4
```

### LỖI HAY GẶP — Không còn shipper nào

File `loi_1.py` — chạy: `python loi_1.py`

```python
don = 17
shipper = 0
print(don // shipper)
```

Lỗi máy báo (cố ý; rút gọn như trên video):

```text
ZeroDivisionError: integer division or
modulo by zero (dòng 3)
```

## Đáp án câu đố Ngày 1

```python
gia = "5000"
print(f"{gia * 2}đ")
```

In ra: `50005000đ`

## Câu đố hôm nay

Ra hai số nào? Đoán trước, rồi chạy thử. Đáp án ở Ngày 3.

```python
print(-7 // 2, -7 % 2)
```

## Bài tập

95 khách, xe 16 chỗ: cần bao nhiêu xe?
