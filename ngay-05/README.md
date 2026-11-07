# Ngày 5 · Comprehension

> Python AI 80 ngày · 1. Python cho người đã biết code · video 1 phút 18 giây

## Bạn học gì

Comprehension: tạo list/dict trong một dòng

## Đáp án câu đố Ngày 4

```python
kho = {"Số Đỏ": 5, "Số Đỏ": 2}
print(len(kho), kho["Số Đỏ"])
```

In ra: `1 2`

## Bài học

_Đi theo đúng thứ tự video. Lời giảng là lời đọc trong video; code và kết quả là bản máy đã chạy thật._

### NGÀY 5 · COMPREHENSION

Câu đố trước: một và hai, khóa trùng bị đè.

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

Dòng này lọc ai tập dưới năm buổi; trợ lý homestay cuối khóa lọc tài liệu y vậy. Nhưng đổi sang ngoặc nhọn, kết quả thành một thứ khác hẳn.

### ĐỔI MỘT CHỮ — Ngoặc vuông thành ngoặc nhọn

Vậy bạn đoán xem, dòng này in ra gì?

File `buoc_2.py` — chạy: `python buoc_2.py`

```python
buoi = {"Lan": 12, "Tú": 3, "Hà": 8}
nhac = {t for t in buoi if buoi[t] < 5}
print(nhac)
```

**Đoán trước khi chạy — Ngoặc nhọn — in ra gì?**

- A. `['Tú']`
- B. `{'Tú'}`
- C. `{'Tú': 3}`

Kết quả (máy đã chạy thật):

```text
{'Tú'}
```

Đáp án đúng: **B**.

Ra Tú, mất số buổi: đây là set, tập hợp không trùng lặp. Muốn ra từ điển thì còn thiếu một dấu.

### Ý chính — BA KIỂU NGOẶC — Một mẫu ba kiểu ngoặc

Đó là dấu hai chấm: có cặp khóa, giá trị thì ra từ điển, không thì tập hợp. Đọc comprehension như lễ tân gym nói một câu: duyệt sổ, ai dưới năm buổi thì lấy tên. Nhưng câu nói dài được, code quá một dòng thì quay về vòng for.

- **[x ...]** — ra list
- **{x ...}** — ra set, không trùng
- **{k: v ...}** — ra dict, tra theo khóa
- **Quá một dòng** — viết vòng for thường

Ghi nhớ nhanh: ngoặc vuông danh sách · ngoặc nhọn tập hợp · có dấu : từ điển

### BIẾN ĐỔI CẢ LOẠT — Đổi giá trị dựng từ điển

Giờ bỏ phần lọc, đổi vế đầu thành buổi nhân một rưỡi là ra số giờ tập.

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

Thêm dấu hai chấm thì dựng luôn từ điển: tên là khóa, buổi nhân mười là điểm. Mẹo dân code: dòng khó đọc thì đọc từ chữ for, vế đầu đọc sau cùng.

### LỖI HAY GẶP — Tưởng dict hóa ra set

Chính dấu hai chấm ấy hay bị quên, và bảng điểm lặng lẽ thành tập hợp.

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

Tra điểm Tú là vỡ: lỗi kiểu TypeError, tập hợp không tra theo tên. Sửa: thêm tên và dấu hai chấm trước giá trị.

## Tóm lại

Tóm lại: ngoặc quyết định kiểu, quá một dòng thì về for. Giờ thì bạn biết vì sao ngoặc nhọn nuốt mất số buổi của Tú.

## Câu đố hôm nay

In ra gì? Đoán trước, rồi chạy thử. Đáp án ở Ngày 6.

```python
buoi = {"Lan": 12, "Tú": 3, "Hà": 8}
print({n > 5 for n in buoi.values()})
```

## Bài tập

Lọc tên ai tập từ 8 buổi, và dict tên → số buổi còn thiếu để đủ 12.
