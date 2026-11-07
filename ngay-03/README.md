# Ngày 3 · Chuỗi & list

> Python AI 80 ngày · 1. Python cho người đã biết code · video 1 phút 15 giây

## Bạn học gì

Chuỗi & list: chỉ số âm và lát cắt [đầu:cuối:bước]

## Đáp án câu đố Ngày 2

```python
print(-7 // 2, -7 % 2)
```

In ra: `-4 1`

## Bài học

_Đi theo đúng thứ tự video. Lời giảng là lời đọc trong video; code và kết quả là bản máy đã chạy thật._

### NGÀY 3 · CHỈ SỐ ÂM & LÁT CẮT

Hôm qua: âm bốn và một. Năm người xếp hàng mua vé, cắt từ một đến ba, mấy người?

File `buoc_1.py` — chạy: `python buoc_1.py`

```python
hang = ["An", "Bảo", "Chi", "Duy", "Em"]
print(hang[1:3])
```

**Đoán trước khi chạy — Bạn cược in ra mấy người?**

- A. `['Bảo', 'Chi']`
- B. `['An', 'Bảo', 'Chi']`
- C. `['Bảo', 'Chi', 'Duy']`

Kết quả (máy đã chạy thật):

```text
['Bảo', 'Chi']
```

Đáp án đúng: **A**.

Chỉ hai, An bị bỏ qua — vì sao?

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

Đó là vì Python đếm từ không: vị trí một là Bảo. Còn âm một là người cuối, khỏi đếm. Lát một đến ba là người thứ hai tới trước người thứ tư. Trợ lý homestay ngày tám mươi cũng cắt lấy ba đoạn tài liệu khớp nhất.

### Ý chính — KHÁI NIỆM — Hai cách gọi, ba ô cắt

Vậy mỗi người có hai số: dương đếm từ đầu, âm từ đuôi. Lát có ba ô đầu, cuối, bước; ô trống là tới mép. Chỉ khác: ngoài đời chẳng ai đứng ở vị trí âm.

- **hang[0]** — người đầu, đếm từ 0
- **hang[-1]** — người cuối, đếm từ đuôi
- **[đầu:cuối]** — không lấy vị trí cuối
- **[::bước]** — bước -1 là đảo ngược

Ghi nhớ nhanh: list và chuỗi · ô trống = tới mép · bước âm đi ngược

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

Giờ thử ô bước: bước âm một lật ngược hàng. Bước hai thì cách một lấy một. Chuỗi cắt y hệt: ghế H mười hai, ký tự đầu là hàng. Phần sau đổi số, cộng một, ra mười ba.

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

Nhưng cắt lố tới chín mươi chín vẫn êm, trả phần có thật. Còn gọi vị trí chín thì ném lỗi chỉ số IndexError: hàng chỉ năm người. Sửa: chỉ gọi từ không đến bốn. Mẹo: tên lỗi luôn nằm ở dòng cuối báo lỗi.

## Tóm lại

Tóm lại: đếm từ không, âm từ đuôi, lát bỏ mép cuối.

## Câu đố hôm nay

Còn lại chữ gì? Đoán trước, rồi chạy thử. Đáp án ở Ngày 4.

```python
ve = "RAPPHIM"
print(ve[::-2])
```

## Bài tập

Lấy 3 người cuối hàng bằng chỉ số âm, rồi in số ghế kế sau "K09".
