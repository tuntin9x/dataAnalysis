Mô tả lại mô hình lập trình MapReduce.
Mapreduce gồm 2 pha : map và reduce.
------------------------------------------------
Bài mô tả gồm 1 máy chủ master và  2 worker.
- Trong bài này có sử dụng thêm cả socket để thực hiện phân tán tính toán
------------------------------------------------
Nguyên lý vận hành:
	- Master sẽ thực hiện nhận dữ liệu vào 1 file cỡ xMB dữ liệu
		+) Loading file 
		+) Thực hiện gửi từng dòng một sang cho worker-map thực hiện hàm map(),
			sau khi worker-map thực hiện xong trả về cho master 
		+) Master thực hiện gửi kết quả của worker-map cho worker-reduce tại đây,
			worker-reduce thực hiện hàm reduce() gửi về cho master
		+) Master thưc hiện tính tổng hợp trên các reduce để ra được kết quả cuối.
	- Worker sẽ thực hiện tính toán 2 hàm là:
		+) map() thực hiện gán giá trị cho mỗi từ là 1
		+) reduce() thực hiện tổng hợp đưa ra tần số của mỗi loại từ
-------------------------------------------------
Hướng dẫn chạy:
	*** LƯU Ý NHỚ CHẠY FILE THEO ĐÚNG THỨ TỰ !!! ***
	1. python3 master.py
	2. python3 worker-map.py
	3. python3 worker-reduce.py
