# Ngày 2 · Số trong Python

> Python AI 80 ngày · 1. Python cho người đã biết code · video 1 phút 17 giây

## Bạn học gì

Số trong Python: /, //, %, int không tràn, round(2.5) = 2

## Đáp án câu đố Ngày 1

```python
gia = "5000"
print(f"{gia * 2}đ")
```

In ra: `50005000đ`

## Bài học

_Đi theo đúng thứ tự video. Lời giảng là lời đọc trong video; code và kết quả là bản máy đã chạy thật._

### NGÀY 2 · SỐ TRONG PYTHON

Hôm qua: chuỗi lặp đôi, ra năm nghìn năm nghìn.

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

Mười bảy đơn chia năm shipper: mỗi người ba phẩy bốn đơn. Ai chở nổi không phẩy bốn đơn? Thêm một gạch thì sao?

### THÊM MỘT GẠCH — Chia lấy phần nguyên

Vậy hai gạch, chia lấy nguyên, bạn đoán ra gì?

File `buoc_2.py` — chạy: `python buoc_2.py`

```python
don = 17
shipper = 5
print(don // shipper)
```

**Đoán trước khi chạy — Mỗi shipper chở mấy đơn?**

- A. `3.4`
- B. `3`
- C. `4`

Kết quả (máy đã chạy thật):

```text
3
```

Đáp án đúng: **B**.

Ba, làm tròn xuống: số đơn chở trọn. Phân trang, chia dữ liệu thành mẻ: dân làm dữ liệu dùng nó hằng ngày.

### PHẦN DƯ VÀ SỐ ÂM — Dư mấy đơn? Số âm thì sao?

Còn hai đơn dư là phép lấy dư, dấu phần trăm.

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

Nhưng với số âm thì khác: âm mười bảy hai gạch năm ra âm bốn. Vì hai gạch làm tròn xuống, khác Java cắt phần lẻ.

### Ý chính — BA PHÉP CHIA + INT — Chia, lấy nguyên, lấy dư

Hóa ra một gạch luôn ra số thực: sáu chia ba ra hai phẩy không. Số nguyên int không có trần: hai mũ sáu mươi tư in đủ. Mẹo dân code: divmod trả thương lẫn dư một lần.

- **/** — luôn ra số thực: 6 / 3 = 2.0
- **//** — làm tròn xuống: -17 // 5 = -4
- **%** — phần dư: 17 % 5 = 2
- **int** — không tràn: 2 ** 64 in đủ

Ghi nhớ nhanh: 6 / 3 = 2.0 · 2 ** 64 20 chữ số · divmod(17, 5) → (3, 2)

### BẪY LÀM TRÒN — round(2.5) ra mấy?

Thế còn hai phẩy năm cây số, làm tròn ra mấy?

File `buoc_4.py` — chạy: `python buoc_4.py`

```python
so_km = 2.5
print(round(so_km), round(so_km + 1))
```

**Đoán trước khi chạy — Bạn cược ra mấy?**

- A. `3 4`
- B. `2 4`
- C. `2 3`

Kết quả (máy đã chạy thật):

```text
2 4
```

Đáp án đúng: **B**.

Ra hai, ba phẩy năm thành bốn: round làm tròn nửa về số chẵn.

### LỖI HAY GẶP — Không còn shipper nào

Khoan, hết shipper, chia cho không thì sao?

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

Python dừng ở dòng chia, báo lỗi ZeroDivisionError. Sửa: kiểm tra shipper khác không trước khi chia.

## Tóm lại

Tóm lại: chở trọn dùng hai gạch, đơn dư dùng phần trăm.

## Câu đố hôm nay

Ra hai số nào? Đoán trước, rồi chạy thử. Đáp án ở Ngày 3.

```python
print(-7 // 2, -7 % 2)
```

## Bài tập

95 khách, xe 16 chỗ: cần bao nhiêu xe?
