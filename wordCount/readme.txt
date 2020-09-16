Mô tả lại mô hình lập trình MapReduce.
Mapreduce gồm 2 pha : map và reduce.
------------------------------------------------
Bài mô tả gồm 1 máy chủ master và  2 worker.
- Trong bài này có sử dụng thêm cả socket để thực hiện phân tán tính toán
------------------------------------------------
Nguyên lý vận hành:
	- Master sẽ thực hiện nhận dữ liệu vào 1 file cỡ 512MB dữ liệu
		Master thực hiện chia dữ liệu dựa trên số worker rảnh dỗi.
		Master thực hiện nhận lại dữ liệu sau khi worker tính toán xong.
	- Worker sẽ thực hiện tính toán 2 hàm là:
		+) map() thực hiện gán giá trị cho mỗi từ là 1
		+) reduce() thực hiện tổng hợp đưa ra tần số của mỗi loại từ

