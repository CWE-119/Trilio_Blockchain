import streamlit as st
from trilio import *
import requests
from streamlit_lottie import st_lottie
import images_link
#

#
# background links
# '''
# link 1 = https://www.wallpaperflare.com/black-and-gray-abstract-digital-wallpaper-digital-art-low-poly-wallpaper-sksm
#
# link 2 = https://www.wallpaperflare.com/white-geometric-artwork-abstract-digital-art-lacza-low-poly-wallpaper-pcwls
#
# 3. https://www.wallpaperflare.com/black-and-white-geometric-digital-wallpaper-low-poly-wireframe-wallpaper-yrk
# 4.https://www.wallpaperflare.com/gray-and-orange-geometric-digital-wallpaper-render-wireframe-wallpaper-phicp
# '''
# def add_bg_from_url():
#     st.markdown(
#         f"{images_link.bg_link}",
#         unsafe_allow_html=True
#     )
#
#
# add_bg_from_url()
#
#
# ethereum animation
def load_lottierurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#
#
# #  ----load assets----
lotte_ethereum = load_lottierurl("https://assets6.lottiefiles.com/packages/lf20_p6ekkqz9.json")
#
# header section
st.subheader("This is a blockchain app build with streamlit")
st_lottie(lotte_ethereum, height=500, key="ethereum")
st.title("blockchain transaction database")

st.header("Blockchain ")


if 'bc' not in st.session_state:
    st.session_state.bc = Trilio()


# block height
height_button = st.button("check height")
if height_button:
    height = len(st.session_state.wallet)
    st.write(f" the block height is {height}")

st.markdown("***")
st.markdown("# create your block first")

if 'wallet' not in st.session_state:
    st.session_state.wallet = []

createBtn = st.button('Create wallet')
if createBtn:
    wallet = st.session_state.bc.Wallet.create_wallet()
    private_KEY = wallet['address']["pve"]
    public_KEY = wallet['address']['pbc']
    st.success("Wallet has been created")
    st.warning(f"your private key :  {private_KEY}")
    st.warning(f"your public key :  {public_KEY}")
    st.session_state.wallet.append(wallet)

# show blocks
if st.button("show al the blocks"):
    st.session_state.wallet


st.markdown("***")
st.markdown("# DO TRANSACTION")
# create transaction
to = st.text_input("to:"),
froms = st.text_input("enter your pve-key"),
amount = st.text_input("enter your amount")

if st.button("to make transaction"):
    transaction = st.session_state.bc.create_transaction(
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
    balance = st.session_state.bc.Wallet.get_balance(private_key=pve, public_key=pub )
    st.success(balance)

# crediting a wallet
st.markdown("***")
st.markdown("crediting a wallet")
st.markdown("- enter the public key for the account where you want to deposit credit")
cred_pub = st.text_input("public key here")
cred_amount = st.text_input("amount of money u want to deposit")
if st.button("make your deposit"):
    credit = st.session_state.bc.Wallet.create_wallet(public_key = str(cred_pub), amount = cred_amount)
    st.success(credit)

# these are the balance details
st.markdown("***")
st.markdown("these are the balance details")

blnc_pve = st.text_input("private key")
blnc_pbc = st.text_input("public key")
if st.button("show that there is zero balance"):
    get_balances = st.session_state.bc.Wallet.get_balance(private_key=blnc_pve, public_key= blnc_pbc)
    st.success(get_balances)

# assets
if st.button("shows that there is no asset currently"):
    asset_bc = st.session_state.bc.Wallet.get_assets(private_key = blnc_pve, public_key=blnc_pbc)
    st.success(asset_bc)

#get collection
if st.button("shows that there are no collections"):
    collections = st.session_state.bc.Wallet.get_collections(private_key=blnc_pve,public_key=blnc_pbc)
    st.success(collections)


# chain validity
st.markdown("***")
st.markdown("# check chain validity")
# st.button(bc.trilio.chain)
status = st.session_state.bc.trilio.chain
if st.button("is chain valid"):
    if status:
        st.header("the chain is valid")
        st.success("chain is valid")
    if not status:
        st.header("the chain is not valid")
        st.error("something went wrong")

# "st.session_state object:" ,st.session_state
#

# if 'wallet' not in st.session_state:
#     st.session_state.wallet = []
#
#
# createBtn = st.button('Create wallet')
# if createBtn:
#     wallet = st.session_state.bc.Wallet.create_wallet()
#     st.session_state.wallet.append(wallet)
#
# "number of wallets: ", len(st.session_state.wallet)
# st.session_state.wallet
