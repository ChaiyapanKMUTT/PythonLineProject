from flask import Flask, request
from linebot import *
from linebot.models import *
from recommentdedFund import input_fund
from fundInfomation import fund_infomation
from recommntdedFund2 import recommend_fund


app = Flask(__name__)

line_bot_api = LineBotApi(
    "HcI6qhZpYNV0g1Lr0enasaOsQkRbP1bHkRkPJ2BK2Rw5N6g9BAyQHJPXGmdfCHoO1SDYhlOtCMaig6taVKn+jvykJbdELhnPJiRACxTt0LhCQ209zCz0YsS8Yh5xmTWnAfBbV2syuDE5Ncb68O+3+QdB04t89/1O/w1cDnyilFU="
)
handler = WebhookHandler("b002ff67c9fcafe1dd1dd2af52224f7e")


@app.route("/callback", methods=["POST"])
def callback():
    body = request.get_data(as_text=True)
    # print(body)
    req = request.get_json(silent=True, force=True)
    intent = req["queryResult"]["intent"]["displayName"]
    text = req["originalDetectIntentRequest"]["payload"]["data"]["message"]["text"]
    reply_token = req["originalDetectIntentRequest"]["payload"]["data"]["replyToken"]
    id = req["originalDetectIntentRequest"]["payload"]["data"]["source"]["userId"]
    disname = line_bot_api.get_profile(id).display_name

    print("id = " + id)
    print("name = " + disname)
    print("text = " + text)
    print("intent = " + intent)
    print("reply_token = " + reply_token)
    

    reply(intent, text, reply_token, id, disname, req)

    return "OK"


def reply(intent, text, reply_token, id, disname, req):
    
    if intent == "Testing":
        text_message = TextSendMessage(text="ทดสอบกลับตอบจาก Flask callback สำเร็จ")
        line_bot_api.reply_message(reply_token, text_message)
    else : 
        fund_name = req["queryResult"]["outputContexts"][1]["parameters"][
        "fund_name.original"
        ]
        main_url = "https://www.finnomena.com/fund/"
        if intent == "FundInfomation - custom - yes":
            fund_info_item = fund_infomation(fund_name)

            if fund_info_item.empty:
                sticker_message = StickerMessage(package_id="6136", sticker_id="10551380")
                text_message = TextSendMessage(text=f"ไม่พบข้อมูลกองทุน {fund_name} ครับ")
                line_bot_api.reply_message(reply_token, [sticker_message, text_message])
            else:
                carousel_template = CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            # เปลี่ยนรูปด้วย
                            thumbnail_image_url="https://i.postimg.cc/3w49jZ2s/Screenshot-2566-12-13-at-12-56-19.png",
                            title=f"กองทุน  {fund_info_item['fund_name'].to_list()[0]}",
                            text=f"จาก {fund_info_item['name_th'].to_list()[0]}",
                            actions=[
                                URIAction(
                                    label="ดูรายละเอียด",
                                    uri=f"{main_url}{fund_info_item['fund_name'].to_list()[0]}".replace(
                                        " ", "%20"
                                    ),
                                ),
                            ],
                        ),
                    ],
                    imageAspectRatio="square",
                    imageSize="contain",
                )

                line_bot_api.reply_message(
                    reply_token,
                    [
                        TextSendMessage(
                            text=f"รายละเอียดกองทุน {fund_info_item['fund_name'].to_list()[0]} "
                        ),
                        TemplateSendMessage(
                            alt_text="รายละเอียดกองทุน",
                            template=carousel_template,
                        ),
                    ],
                )
        elif intent == "RecommetFund - custom - yes":
            recommend_items = recommend_fund(fund_name)

            if len(recommend_items) == 1:
                sticker_message = StickerSendMessage(
                    package_id="6136", sticker_id="10551380"
                )
                text_message = TextSendMessage(
                    text=f"กองทุน {fund_name}  {recommend_items[0]}"
                )
                line_bot_api.reply_message(reply_token, [sticker_message, text_message])
            else:
                carousel_template = CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url="https://i.postimg.cc/t4DW8RBv/Screenshot-2566-11-20-at-16-08-50.png",
                            text=f"กองทุน  {recommend_items[0]}",
                            title=recommend_items[0],
                            actions=[
                                URIAction(
                                    label="ดูรายละเอียด",
                                    uri=f"{main_url}{recommend_items[0]}".replace(
                                        " ", "%20"
                                    ),
                                ),
                            ],
                        ),
                        CarouselColumn(
                            thumbnail_image_url="https://i.postimg.cc/BZmWZkm8/Screenshot-2566-11-20-at-17-33-39.png",
                            text=f"กองทุน  {recommend_items[1]}",
                            title=recommend_items[1],
                            actions=[
                                URIAction(
                                    label="ดูรายละเอียด",
                                    uri=f"{main_url}{recommend_items[1]}".replace(
                                        " ", "%20"
                                    ),
                                ),
                            ],
                        ),
                        CarouselColumn(
                            thumbnail_image_url="https://i.postimg.cc/d33TMg0M/Screenshot-2566-11-20-at-17-41-24.png",
                            text=f"กองทุน  {recommend_items[2]}",
                            title=recommend_items[2],
                            actions=[
                                URIAction(
                                    label="ดูรายละเอียด",
                                    uri=f"{main_url}{recommend_items[2]}".replace(
                                        " ", "%20"
                                    ),
                                ),
                            ],
                        ),
                        CarouselColumn(
                            thumbnail_image_url="https://i.postimg.cc/Tw9P30sR/Screenshot-2566-11-20-at-17-37-53.png",
                            text=f"กองทุน  {recommend_items[3]}",
                            title=recommend_items[3],
                            actions=[
                                URIAction(
                                    label="ดูรายละเอียด",
                                    uri=f"{main_url}{recommend_items[3]}".replace(
                                        " ", "%20"
                                    ),
                                ),
                            ],
                        ),
                        CarouselColumn(
                            thumbnail_image_url="https://i.postimg.cc/fTjjcQ0C/Screenshot-2566-11-20-at-17-46-00.png",
                            text=f"กองทุน  {recommend_items[4]}",
                            title=recommend_items[4],
                            actions=[
                                URIAction(
                                    label="ดูรายละเอียด",
                                    uri=f"{main_url}{recommend_items[4]}".replace(
                                        " ", "%20"
                                    ),
                                ),
                            ],
                        ),
                    ],
                    imageAspectRatio="square",
                    imageSize="contain",
                )

            line_bot_api.reply_message(
                reply_token,
                [
                    TextSendMessage(text=f"แนะนำกองทุน ที่ซื้อร่วมกันกับ {fund_name}"),
                    TemplateSendMessage(
                        alt_text="แนะนำกองทุน",
                        template=carousel_template,
                    ),
                    TextSendMessage(text=f"การลงทุนมีความเสี่ยง ผู้ลงทุนควรศึกษาข้อมูลให้รอบคอบก่อนตัดสินใจลงทุน")
                ],
            )


if __name__ == "__main__":
    app.run(debug=True, port=5002)
