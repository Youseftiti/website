import requests
from PIL import Image# بيلو هاي مكتبه بنزلها مشان اقدر استخدم الصور
import streamlit as st
import datetime
from streamlit_lottie import st_lottie#مكتبه خاصه بالانيميشن


st.set_page_config(page_title="my web",page_icon=":🤖",layout="wide")
#-----------------------------
def load_lottieurl(url):#هاذ فنقشن ليدخل على معلومات الجيسون لل لوتي انيميشن 
    r = requests.get(url)#امر احضار اسم موقع او هان الصوره المتحركه 
    if r.status_code != 200:#لازم يكوم كود الجيسون لللوتي انيميشن 200 واذا ما بساوي 200برجعnone
        return None#اذا صار خطا راح يرجع ولا اشي
    return r.json()#هاي تعني انو ؤاح يحضر الجاسيون ديتا للرسمه الي طلبتها

#-----------------------------
#تعريف متغير واعطي الفنكشن الي  عملتو الي هو فنكشن احضار الurl الخاص بالصوره
lottie_coding = load_lottieurl ("https://lottie.host/acd4db34-3695-4dba-9cce-91c78c74486f/HkRkLBz1Yb.json")
# بدي لحط الدايركتري للصور في متغير مشان استخدمو
img_contact_from = Image.open("imge/imgcod.png")
img_contact_from2 = Image.open("imge/food.png")
#use local css
def local_css(file_name):#هذا الفنقشن مشان اجيب التصميم من ملف السي اس اس الي مخزنو في البرنامج
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


with st.chat_message("user"):
    st.write(" # Hello 🤧")
with st.container():#فقط من اجل ترتيب الكود يمكن للموقع العمل دونها
     st.subheader("  hi, i am youse 🏴🏁:")
     st.subheader("YOUSEF")#"hhhhhhhhhh"
     st.title("fdfgdfgdfg")
     st.write("jjjdfgkbnbnkkkjjj")
     st.write("[learn more>](https://python.org)")

d = st.date_input("When's your birthday", value=None)
st.write('Your birthday is:', d)

print("yfj")

#-------------------------
with st.container():
     st.write("---")#هاي بتعطي فاصل طولي على الصفحه خط كامل 
     left_column, right_column =st.columns(2)
     with left_column:
        st.header("WHAT I DO")
        st.write("##")
        st.write("""
              
              # The advent of large language models like GPT has revolutionized the ease of developing chat-based applications. 
              Streamlit offers several Chat elements, enabling you to build Graphical User Interfaces (GUIs) for conversational agents or chatbots.
               Leveraging session state along with these elements allows you to construct anything from a basic chatbot to a more advanced, 
              ChatGPT-like experience using purely Python code.
              
              
              
              
              """)
        st.write("[LINKE>](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps)")
     with right_column:
         st_lottie(lottie_coding, height=300, key="coding")
         

#هان بناء المشروع نفسه
with st.container():#كونتينر مشان احط في الاعمده ويكون الشغل مرتب زي حاوي للمشروع
    st.write("---")#فاصل افقي خط
    st.header("MY PROJECTS")
    st.write("##")
    image_column, text_column = st.columns((1,2))#بدي عامودين وبدي العامود الثاني ضعف العامود الاول 
    with image_column:
        st.write("##")
        #بدي احط صوره
        st.image(img_contact_from)
    with text_column:
        st.subheader("first project")
        st.write(
            """
                 
                 
                 https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps

              
             """

        )
        st.markdown("[watch video](https://www.youtube.com/watch?v=VqgUkExPvLY&t=286s)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_from2)
    with text_column:
        st.subheader("next project")    
        st.write(
            """
           The advent of large language models like GPT has revolutionized the ease of developing chat-based applications.
           Streamlit offers several Chat elements, enabling you to build Graphical User Interfaces (GUIs) for conversational agents or chatbots.
           Leveraging session state along with these elements allows you to construct anything from a basic chatbot to a more advanced, 
           ChatGPT-like experience using purely Python code.
            """
        )
        st.markdown("[LINK](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps)")

#----------------contact-------------تواصلو معي 
with st.container():
    st.write("---")
    st.header("GET IN TOUCH")
    st.write("##")#اعطاء مساحه بسيطه
    

    contact_form = """
              <form action="https://formsubmit.co/youseftiti08@gmail.com" method="POST">
              <input type="hidden" name="_captcha" value="false">هاي كود مشان يخفي التحقق من الايميل يعني يسهل على المستخدم يرسل ايميل بدون تحقق
     <input type="text" name="name" placeholder ="your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="your message here" required></textarea>
     <button type="submit">Send</button>
     <button type = "need"> need</button>
</form>
            

       """
    left_column, right_column =st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

