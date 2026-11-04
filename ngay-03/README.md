# Ngày 3 · Chuỗi & list

Python AI 80 ngày · 1. Python cho người đã biết code

## Bạn học gì

Chuỗi & list: chỉ số âm và lát cắt [đầu:cuối:bước]

## Code trong video

### NGÀY 3 · CHỈ SỐ ÂM & LÁT CẮT

File `buoc_1.py` — chạy: `python buoc_1.py`

```python
hang = ["An", "Bảo", "Chi", "Duy", "Em"]
print(hang[1:3])
```

Kết quả (máy đã chạy thật):

```text
['Bảo', 'Chi']
```

### ĐẾM TỪ ĐÂU — Đếm từ số không

File `buoc_2.py` — chạy: `python buoc_2.py`

```python
hang = ["An", "Bảo", "Chi", "Duy", "Em"]
print(hang[0], hang[-1])
print(hang[1:3])
```

Kết quả (máy đã chạy thật):

```text
An Em
['Bảo', 'Chi']
```

### Ô BƯỚC & CHUỖI — Bước nhảy và chuỗi

File `buoc_3.py` — chạy: `python buoc_3.py`

```python
hang = ["An", "Bảo", "Chi", "Duy", "Em"]
print(hang[::-1])
print(hang[::2])
ghe = "H12"
print(ghe[0], int(ghe[1:]) + 1)
```

Kết quả (máy đã chạy thật):

```text
['Em', 'Duy', 'Chi', 'Bảo', 'An']
['An', 'Chi', 'Em']
H 13
```

### LỖI HAY GẶP — Cắt lố êm, gọi lố lỗi

File `loi_1.py` — chạy: `python loi_1.py`

```python
hang = ["An", "Bảo", "Chi", "Duy", "Em"]
print(hang[1:99])
print(hang[9])
```

Lỗi máy báo (cố ý; rút gọn như trên video):

```text
['Bảo', 'Chi', 'Duy', 'Em']
IndexError: list index out of range (dòng
3)
```

## Đáp án câu đố Ngày 2

```python
print(-7 // 2, -7 % 2)
```

In ra: `-4 1`

## Câu đố hôm nay

Còn lại chữ gì? Đoán trước, rồi chạy thử. Đáp án ở Ngày 4.

```python
ve = "RAPPHIM"
print(ve[::-2])
```

## Bài tập

Lấy 3 người cuối hàng bằng chỉ số âm, rồi in số ghế kế sau "K09".
