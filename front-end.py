import streamlit as st
from trilio import *
import requests
from streamlit_lottie import st_lottie


# background links
# '''
# link 1 = https://www.wallpaperflare.com/black-and-gray-abstract-digital-wallpaper-digital-art-low-poly-wallpaper-sksm
#
# link 2 = https://www.wallpaperflare.com/white-geometric-artwork-abstract-digital-art-lacza-low-poly-wallpaper-pcwls
#
# 3. https://www.wallpaperflare.com/black-and-white-geometric-digital-wallpaper-low-poly-wireframe-wallpaper-yrk
# 4.https://www.wallpaperflare.com/gray-and-orange-geometric-digital-wallpaper-render-wireframe-wallpaper-phicp
# '''
def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-attachment: ;
             background-size:cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()


# ethereum animation
def load_lottierurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#  ----load assets----
lotte_ethereum = load_lottierurl("https://assets6.lottiefiles.com/packages/lf20_p6ekkqz9.json")

# header section
st.subheader("This is a blockchain app build with streamlit")
st_lottie(lotte_ethereum, height=500, key="ethereum")
with st.container():
    # left_column, right_column = st.columns(2)
    # with left_column:
    # title
    st.title("blockchain transaction database")
# with right_column:
#     st_lottie(lotte_ethereum, height=150, key="ethereum")
# header
st.header("Blockchain ")
# name = st.text_input("enter the name of your block", )
# data = name
st.markdown("***")
st.markdown("# create your block first")
with st.container():
    bc = Trilio()
    if st.button("press to create wallet"):
        wallet = bc.Wallet.create_wallet()
        st.success(wallet)

    st.markdown("***")
    st.markdown("# DO TRANSACTION")
    # create transaction
    to = st.text_input("to:"),
    froms = st.text_input("enter your pve-key"),
    amount = st.text_input("enter your amount")

    if st.button("to make transaction"):
        transaction = bc.create_transaction(
            datetime.now(),
            data={
                "type": "token-transfer",
                "data": {
                    "to": to,
                    "from": froms,
                    "amount": amount,
                }
            }
        )
        st.success("the transaction has succeed")

    st.markdown("***")
    st.markdown("# check your balance")
    # check balance
    pve = st.text_input("your private key")
    pub = st.text_input("your public key")
    if st.button("check your balance"):
        balance = bc.Wallet.get_balance(private_key=pve, public_key=pub )
        st.success(balance)

    # crediting a wallet
    st.markdown("***")
    st.markdown("crediting a wallet")
    st.markdown("- enter the public key for the account where you want to deposit credit")
    cred_pub = st.text_input("public key here")
    cred_amount = st.text_input("amount of money u want to deposit")
    if st.button("make your deposit"):
        credit = bc.Wallet.create_wallet(public_key = cred_pub, amount = cred_amount)
        st.success(credit)

    # chain validity
    st.markdown("***")
    st.markdown("# check validity")
    # st.button(bc.trilio.chain)
    status = bc.trilio.chain
    if st.button("is chain valid"):
        if status:
            st.header("the chain is valid")
            st.success("chain is valid")
        if not status:
            st.header("the chain is not valid")
            st.error("something went wrong")