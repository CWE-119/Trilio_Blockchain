import streamlit as st
from trilio import *
import requests
from streamlit_lottie import st_lottie
import images_link
#

#
# background links (no image used as backgroung)
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
st.title("Simple Blockchain Project")

# assigned Trilio as bc and storing data in session state
if 'bc' not in st.session_state:
    st.session_state.bc = Trilio()

# storing the data of wallet in session state
if 'wallet' not in st.session_state:
    st.session_state.wallet = []

if "pub_keys" not in st.session_state:
    st.session_state.pub_keys = []

# block height
height = len(st.session_state.wallet)
st.markdown(f"# the chain height is {height}")
if st.button("refresh height size"):
    st.success("refreshed")
st.markdown("***")
st.markdown("# create your block first")



createBtn = st.button('Create wallet')
if createBtn:
    wallet = st.session_state.bc.Wallet.create_wallet()
    private_KEY = wallet['address']["pve"]
    public_KEY = wallet['address']['pbc']
    st.session_state.pub_keys.append(public_KEY)
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
reciver_public_key = st.text_input("reciver_public_key:"),
your_private_key = st.text_input("enter your pve-key"),
amount = st.text_input("enter your amount")

# todo fix the 'to' and 'from' in the transaction , check Trilio_Blockchain_main,pu line 68 to 78

if st.button("to make transaction"):
    transaction = st.session_state.bc.create_transaction(
        datetime.now(),
        data={
            "type": "token-transfer",
            "data": {
                "to": reciver_public_key,
                "from": your_private_key,
                "amount": float(amount),
            }
        }
    )
    st.success("the transaction has succeed")
    st.session_state.wallet


# check balance
st.markdown("***")
st.markdown("# check your balance")
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
    if cred_pub in st.session_state.pub_keys:
        credit = st.session_state.bc.Wallet.credit_wallet(public_key = str(cred_pub), amount = cred_amount)
        st.success(credit)
    else:
        st.error("No public key matches with this public key")


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
valid = st.session_state.bc.validate_chain()
# chain = st.session_state.bc.chain

if st.button("is chain valid"):
    if  height == 0:
        st.error("there is no blocks")
    else:
        if valid == True:
            st.error("chain is not valid")
        else:
            st.success("chain is valid")


# checking session state

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
