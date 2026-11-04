# Ngày 4 · dict, tuple, set

Python AI 80 ngày · 1. Python cho người đã biết code

## Bạn học gì

dict, tuple, set: tra theo khóa, gói nhiều giá trị, bỏ trùng

## Code trong video

### NGÀY 4 · DICT, TUPLE, SET

File `loi_1.py` — chạy: `python loi_1.py`

```python
kho = {"Dế Mèn": 12, "Tắt Đèn": 0}
print(kho["Dế Mèn"])
print(kho["Lão Hạc"])
```

Lỗi máy báo (cố ý; rút gọn như trên video):

```text
12
KeyError: 'Lão Hạc' (dòng 3)
```

### ĐỔI SANG GET — Hỏi bằng get có mặc định

File `buoc_1.py` — chạy: `python buoc_1.py`

```python
kho = {"Dế Mèn": 12, "Tắt Đèn": 0}
print(kho["Dế Mèn"])
print(kho.get("Lão Hạc", 0))
```

Kết quả (máy đã chạy thật):

```text
12
0
```

### GHI VÀ DUYỆT SỔ — Thêm, đè và duyệt sổ

File `buoc_2.py` — chạy: `python buoc_2.py`

```python
kho = {"Dế Mèn": 12, "Tắt Đèn": 0}
kho["Số Đỏ"] = 5
kho["Dế Mèn"] = 9
for ten, sl in kho.items():
    print(ten, sl)
```

Kết quả (máy đã chạy thật):

```text
Dế Mèn 9
Tắt Đèn 0
Số Đỏ 5
```

### SET BỎ TRÙNG — Set tự bỏ trùng

File `buoc_3.py` — chạy: `python buoc_3.py`

```python
the_loai = {"truyện", "thơ", "truyện"}
print(len(the_loai))
```

Kết quả (máy đã chạy thật):

```text
2
```

### LỖI HAY GẶP — Set không có vị trí

File `loi_2.py` — chạy: `python loi_2.py`

```python
the_loai = {"truyện", "thơ", "truyện"}
print(len(the_loai))
print(the_loai[0])
```

Lỗi máy báo (cố ý; rút gọn như trên video):

```text
2
TypeError: 'set' object is not
subscriptable (dòng 3)
```

## Đáp án câu đố Ngày 3

```python
ve = "RAPPHIM"
print(ve[::-2])
```

In ra: `MHPR`

## Câu đố hôm nay

Hai số in ra là gì? Đoán trước, rồi chạy thử. Đáp án ở Ngày 5.

```python
kho = {"Số Đỏ": 5, "Số Đỏ": 2}
print(len(kho), kho["Số Đỏ"])
```

## Bài tập

Đếm số đầu sách còn hàng (sl > 0) và in tên chúng.
