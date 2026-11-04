# Ngày 5 · Comprehension

Python AI 80 ngày · 1. Python cho người đã biết code

## Bạn học gì

Comprehension: tạo list/dict trong một dòng

## Code trong video

### NGÀY 5 · COMPREHENSION

File `buoc_1.py` — chạy: `python buoc_1.py`

```python
buoi = {"Lan": 12, "Tú": 3, "Hà": 8}
nhac = [t for t in buoi if buoi[t] < 5]
print(nhac)
```

Kết quả (máy đã chạy thật):

```text
['Tú']
```

### ĐỔI MỘT CHỮ — Ngoặc vuông thành ngoặc nhọn

File `buoc_2.py` — chạy: `python buoc_2.py`

```python
buoi = {"Lan": 12, "Tú": 3, "Hà": 8}
nhac = {t for t in buoi if buoi[t] < 5}
print(nhac)
```

Kết quả (máy đã chạy thật):

```text
{'Tú'}
```

### BIẾN ĐỔI CẢ LOẠT — Đổi giá trị dựng từ điển

File `buoc_3.py` — chạy: `python buoc_3.py`

```python
buoi = {"Lan": 12, "Tú": 3, "Hà": 8}
gio = [n * 1.5 for n in buoi.values()]
print(gio)
diem = {t: buoi[t] * 10 for t in buoi}
print(diem)
```

Kết quả (máy đã chạy thật):

```text
[18.0, 4.5, 12.0]
{'Lan': 120, 'Tú': 30, 'Hà': 80}
```

### LỖI HAY GẶP — Tưởng dict hóa ra set

File `loi_1.py` — chạy: `python loi_1.py`

```python
buoi = {"Lan": 12, "Tú": 3, "Hà": 8}
diem = {buoi[t] * 10 for t in buoi}
print(diem["Tú"])
```

Lỗi máy báo (cố ý; rút gọn như trên video):

```text
TypeError: 'set' object is not
subscriptable (dòng 3)
```

## Đáp án câu đố Ngày 4

```python
kho = {"Số Đỏ": 5, "Số Đỏ": 2}
print(len(kho), kho["Số Đỏ"])
```

In ra: `1 2`

## Câu đố hôm nay

In ra gì? Đoán trước, rồi chạy thử. Đáp án ở Ngày 6.

```python
buoi = {"Lan": 12, "Tú": 3, "Hà": 8}
print({n > 5 for n in buoi.values()})
```

## Bài tập

Lọc tên ai tập từ 8 buổi, và dict tên → số buổi còn thiếu để đủ 12.
