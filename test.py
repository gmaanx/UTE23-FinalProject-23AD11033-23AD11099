# Import các thư viện cần thiết
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.linear_model import LogisticRegression         
from sklearn.pipeline import make_pipeline                  

# du lieu mau: moi muc bao gom cac cau hoi (cauhoi) va cau tra loi tuong ung voi tung muc (traloi)
du_lieu = {
    "chao_hoi": {
        "cauhoi": [
            "hello",
            "xin chao",
            "chao"
        ],
        "traloi": [
            "Xin chào bạn! Mình có thể giúp gì cho bạn nào?"
        ]
    },
    "nganh_hoc": {
        "cauhoi": [
            "Tôi muốn biết các ngành học của trường",
            "Trường có những ngành nào?",
            "Các ngành đào tạo tại trường là gì?"
        ],
        "traloi": [
            "Trường đào tạo các ngành: Kỹ thuật phần mềm, Cơ khí, Điện tử, v.v."
        ]
    },
    "diem_chuan": {
        "cauhoi": [
            "Điểm chuẩn của ngành Công nghệ thông tin là bao nhiêu?",
            "Tôi muốn biết điểm chuẩn của ngành Kỹ thuật",
            "Điểm chuẩn năm nay như thế nào?"
        ],
        "traloi": [
            "Điểm chuẩn của các ngành thường dao động từ 25 đến 30 điểm, tùy ngành."
        ]
    },
    "hoc_phi": {
        "cauhoi": [
            "Học phí của trường là bao nhiêu?",
            "Tôi cần biết mức học phí của các ngành",
            "Học phí trung bình của trường?"
        ],
        "traloi": [
            "Học phí của trường dao động từ 5 triệu đến 10 triệu đồng mỗi năm, tùy ngành."
        ]
    },
    "hoc_bong": {
        "cauhoi": [
            "Trường có học bổng không?",
            "Tôi muốn biết thông tin về học bổng",
            "Các học bổng dành cho sinh viên?"
        ],
        "traloi": [
            "Trường có nhiều chương trình học bổng, bao gồm học bổng thành tích và học bổng nhu cầu."
        ]
    },
    "dang_ky": {
        "cauhoi": [
            "Làm sao để đăng ký xét tuyển?",
            "Quy trình đăng ký của trường là gì?",
            "Tôi muốn biết cách đăng ký xét tuyển"
        ],
        "traloi": [
            "Để đăng ký xét tuyển, bạn cần truy cập trang web của trường và làm theo hướng dẫn."
        ]
    }
}

# chuan bi du lieu dung de huan luyen: tao cac cau hoi (ds_cauhoi) va nhan (nhan) ung voi tung muc
ds_cauhoi = []
nhan = []
for intent, thongtin in du_lieu.items():
    for cauhoi in thongtin["cauhoi"]:
        ds_cauhoi.append(cauhoi)
        nhan.append(intent)

# tao pipeline ket hop TF-IDF Vectorizer va Logistic Regression
mo_hinh = make_pipeline(TfidfVectorizer(), LogisticRegression())

# huan luyen mo hinh voi du lieu mau
mo_hinh.fit(ds_cauhoi, nhan)

# giao tiep voi user
print("Xin chao, Toi co the giup gi cho ban?")

while True:
    cau_nguoi_dung = input("You: ")
    if cau_nguoi_dung.lower() == "exit":
        print("Chatbot: Tam biet ban nhe!")
        break

    # du doan muc dich cau hoi cua user
    intent = mo_hinh.predict([cau_nguoi_dung])[0]

    # lay cau tra loi de tra loi dua tren du doan muc dich duoc hoi cua user
    tra_loi = du_lieu[intent]["traloi"][0]
    print("Chatbot:", tra_loi)
