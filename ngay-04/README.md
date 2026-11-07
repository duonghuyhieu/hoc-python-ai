# Ngày 4 · dict, tuple, set

> Python AI 80 ngày · 1. Python cho người đã biết code · video 1 phút 13 giây

## Bạn học gì

dict, tuple, set: tra theo khóa, gói nhiều giá trị, bỏ trùng

## Đáp án câu đố Ngày 3

```python
ve = "RAPPHIM"
print(ve[::-2])
```

In ra: `MHPR`

## Bài học

_Đi theo đúng thứ tự video. Lời giảng là lời đọc trong video; code và kết quả là bản máy đã chạy thật._

### NGÀY 4 · DICT, TUPLE, SET

Hôm qua: MHPR.

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

Hỏi Lão Hạc chưa có trong sổ, cả chương trình sập. Thiếu một cuốn sao sập cả, chữ nào cứu?

### ĐỔI SANG GET — Hỏi bằng get có mặc định

Thủ phạm là ngoặc vuông: thiếu khóa là lỗi khóa KeyError.

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

Đổi sang hàm get kèm mặc định, sách vắng ra không. Trợ lý homestay ngày tám mươi tra tài liệu theo khóa đúng kiểu này.

### Ý chính — KHÁI NIỆM — Ba kiểu gom dữ liệu

Vậy sổ kho là dict: tên sách là khóa, số cuốn là giá trị. Khác sổ giấy, sách nào cũng chỉ một dòng. Tuple gói vài giá trị cố định, không sửa được. Còn set là túi bỏ trùng, không thứ tự.

- **dict** — khóa → giá trị, tra nhanh
- **tuple** — gói cố định, không sửa
- **set** — bỏ trùng, không thứ tự

Ghi nhớ nhanh: tra theo khóa · gói cố định · bỏ trùng

### GHI VÀ DUYỆT SỔ — Thêm, đè và duyệt sổ

Quay lại sổ: gán khóa mới là thêm, khóa cũ là đè. Hàm items trả từng tuple tên và số, mở gói thành hai biến.

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

Dế Mèn còn chín, Số Đỏ đứng cuối vì ghi sau.

### SET BỎ TRÙNG — Set tự bỏ trùng

Còn thể loại: ghi truyện hai lần vào set, đếm ra mấy?

File `buoc_3.py` — chạy: `python buoc_3.py`

```python
the_loai = {"truyện", "thơ", "truyện"}
print(len(the_loai))
```

**Đoán trước khi chạy — Đếm ra mấy thể loại?**

- A. `3`
- B. `2`
- C. `Lỗi khi chạy`

Kết quả (máy đã chạy thật):

```text
2
```

Đáp án đúng: **B**.

Ra hai; mẹo dân code: bọc danh sách vào set để lọc trùng.

### LỖI HAY GẶP — Set không có vị trí

Nhưng lấy vị trí không thì vỡ: túi này không có thứ tự.

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

Lỗi kiểu TypeError; sửa một ô của gói cố định cũng thế. Cần thứ tự thì xếp bằng sorted trước.

## Tóm lại

Tóm lại: tra bằng get, sách vắng là không, sổ chẳng sập.

## Câu đố hôm nay

Hai số in ra là gì? Đoán trước, rồi chạy thử. Đáp án ở Ngày 5.

```python
kho = {"Số Đỏ": 5, "Số Đỏ": 2}
print(len(kho), kho["Số Đỏ"])
```

## Bài tập

Đếm số đầu sách còn hàng (sl > 0) và in tên chúng.
