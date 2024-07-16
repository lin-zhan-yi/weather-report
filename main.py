import imager
import weather
from PIL import Image,ImageDraw,ImageFont


title_dict={
    # "日期":[760,160],
    "天氣":[830,160],
    "氣溫":[1160, 160],
    "降雨":[1360, 160],
    "舒適度":[1610, 160],
}

def weather_words(weather):
    feel_dict={
        '寒冷至稍有寒意': 'cold',
        '寒冷至舒適':'slightly cold',
        '非常寒冷':'very cold',
        '陰時多雲短暫雨':'cloudy',
        '陰有雨':'cloudy',
        '多雲短暫雨':'cloudy',
        '多雲時陰':'cloudy',
        '多雲':'partly cloudy',
        '晴時多雲':'cludy',
        '陰短暫陣雨或雷雨':'brief showers or thunderstorms',
        '陰短暫陣雨':'Cloudy with brief showers',
        '多雲時陰短暫陣雨':'Cloudy with brief showers',
        '陰時多雲短暫陣雨或雷雨':'Cloudy with brief showers or thunderstorms',
        '多雲時晴' :'Cloudy and sunny'
    }
    return f"weather {feel_dict[weather]}"

if __name__=="__main__":
    weather_list=weather.getWeatherData()
    date_dict={
        "year":"",
        "month":"",
        "datatime":[],
    }

    for index, item in enumerate(weather_list):
        time = item["startTime"]
        tmp_list = time.split("-")
        if index==0:
            date_dict["year"]=tmp_list[0]
            date_dict["month"]=tmp_list[1]
        time_list=tmp_list[2].split(" ")
        datetime_list=[time_list[0],time_list[1][:-3]]
        date_dict["datatime"].append(datetime_list)

        if index == len(weather_list)-1:
            time = item["endTime"]
            tmp_list = time.split("-")
            time_list = tmp_list[2].split(" ")
            datetime_list = [time_list[0], time_list[1][:-3]]
            date_dict["datatime"].append(datetime_list)
        print(date_dict)

    background_list=imager.getBackground(weather=weather_words(weather_list[0]["Wx"]),count=5)
    if background_list is not None:
        Noto = ImageFont.truetype('assets/NotoSansTC-VariableFont_wght.ttf', size=40)
        print("notosans",Noto.get_variation_names())
        rubik = ImageFont.truetype('assets/Rubik-VariableFont_wght.ttf', size=40)

        for index,background in enumerate(background_list):
            weather_image=Image.new("RGBA",(1920,1080),color=10)
            weather_image.paste(background,(0,0))
            weather_data_box=ImageDraw.Draw(weather_image)

            black_layer = Image.new("RGBA",(1920,1080))
            black_draw = ImageDraw.Draw(black_layer,"RGBA")
            black_draw.rectangle(xy=(0,0,1920,1080),fill=(0,0,0,100))
            black_layer.putalpha(100)

            weather_image.paste(Image.alpha_composite(weather_image,black_layer))

            for key,value in title_dict.items():
                weather_data_box.text(
                    value,
                    key,
                    fill=(255, 255, 255), anchor="ma", font=Noto
                )

            for order,item in enumerate(weather_list):

                weather_data_box.text(
                    (title_dict["天氣"][0], 300 + 200 * order),
                    f"{item['Wx']}",
                    fill=(255, 255, 255), anchor="ma", font=Noto
                )

                weather_data_box.text(
                    (title_dict["氣溫"][0], 300 + 200 * order),
                    f"{item['MinT']}~{item['MaxT']}",
                    fill=(255, 255, 255), anchor="ma", font=Noto
                )

                weather_data_box.text(
                    (title_dict["降雨"][0], 300 + 200 * order),
                    f"{item['PoP']}",
                    fill=(255, 255, 255), anchor="ma", font=Noto
                )

                weather_data_box.text(
                    (title_dict["舒適度"][0], 300 + 200 * order),
                    f"{item['CI']}",
                    fill=(255, 255, 255), anchor="ma", font=Noto
                )

            Noto = ImageFont.truetype('assets/NotoSansTC-VariableFont_wght.ttf', size=80)
            Noto.set_variation_by_name("Bold")
            weather_data_box.text(
                (230,80),
                date_dict["year"],
                fill=(255, 255, 255), anchor="ma", font=Noto
            )
            Noto = ImageFont.truetype('assets/NotoSansTC-VariableFont_wght.ttf', size=80)
            Noto.set_variation_by_name("Bold")
            weather_data_box.text(
                (425, 80),
                f'{date_dict["month"]}月',
                fill=(255, 255, 255), anchor="ma", font=Noto
            )
            for order,item in enumerate(date_dict["datatime"]):
                Noto = ImageFont.truetype('assets/NotoSansTC-VariableFont_wght.ttf', size=80)
                Noto.set_variation_by_name("Bold")
                weather_data_box.text(
                    (390, 180+200*order),item[0],
                    fill=(255, 255, 255), anchor="ma", font=Noto
                )
                Noto = ImageFont.truetype('assets/NotoSansTC-VariableFont_wght.ttf', size=40)
                Noto.set_variation_by_name("Regular")
                weather_data_box.text(
                    (500, 225 + 200 * order), item[1],
                    fill=(255, 255, 255), anchor="ma", font=Noto
                )

                weather_data_box.line((550 ,250+200*order, 1800, 250+200*order))
                weather_data_box.line((100, 250 + 200 * order, 300, 250 + 200 * order))
            file_name=f"result.png"
            weather_image.save(file_name)
    else:
        print("取得照片失敗")
