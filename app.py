from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

EMPLOYEES = [
    "孙鑫","管炜","唐启豪","李雪慧","柯汉钟","郑泽晓","周彦梓","郭志强",
    "吴子桐","陈溥林","金翔","黎炜祺","宋志杰","朱晓彬","陈雨蒙","李泳仪",
    "王宇璇","周倩昀","郭泽鑫","蒋焯豪","潘舒扬","马伊帆2号","陈森豪",
    "莫绵","朱子怡","冯志源","林梓楠","兰海涵","吴哲远","魏曾力",
    "张富士","熊喆","吴昊5号","佘志鸿","赵振飞"
]

checked_in = set()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    message_type = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()

        if not name:
            message = "请输入姓名"
            message_type = "error"
        elif name not in EMPLOYEES:
            message = "姓名不在运营部名单中，请检查"
            message_type = "error"
        elif name in checked_in:
            message = f"{name}，你已经签到过了"
            message_type = "error"
        else:
            checked_in.add(name)
            message = f"{name}，签到成功！"
            message_type = "success"

    signed = sorted(list(checked_in))
    unsigned = [n for n in EMPLOYEES if n not in checked_in]

    return render_template(
        "index.html",
        signed=signed,
        unsigned=unsigned,
        signed_count=len(signed),
        unsigned_count=len(unsigned),
        total=len(EMPLOYEES),
        message=message,
        message_type=message_type
    )

@app.route("/reset", methods=["POST"])
def reset():
    checked_in.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
