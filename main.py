import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Restaurant Bill Generator",
    page_icon="🍔",
    layout="wide"
)

# -------------------------------
# Custom CSS
# -------------------------------

st.markdown("""
<style>

/* ===============================
   MAIN ATTRACTIVE BACKGROUND
   =============================== */

.stApp {
    background:
        radial-gradient(
            circle at 10% 20%,
            rgba(255, 99, 71, 0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(255, 193, 7, 0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 80% 85%,
            rgba(156, 39, 176, 0.15),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #fff7ed 0%,
            #fff 35%,
            #f5f3ff 70%,
            #eef9ff 100%
        );

    background-attachment: fixed;
}


/* Decorative background glow */

.stApp::before {
    content: "";
    position: fixed;
    width: 300px;
    height: 300px;
    top: 80px;
    left: -100px;
    background: rgba(255, 87, 34, 0.10);
    border-radius: 50%;
    filter: blur(70px);
    z-index: -1;
}

.stApp::after {
    content: "";
    position: fixed;
    width: 350px;
    height: 350px;
    bottom: 50px;
    right: -120px;
    background: rgba(103, 58, 183, 0.10);
    border-radius: 50%;
    filter: blur(80px);
    z-index: -1;
}


/* ===============================
   TITLE
   =============================== */

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;

    background: linear-gradient(
        90deg,
        #ff512f,
        #dd2476,
        #7b2ff7
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    text-shadow: 0px 3px 15px rgba(221, 36, 118, 0.12);
}


/* ===============================
   SUBTITLE
   =============================== */

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555555;
    margin-bottom: 30px;
}


/* ===============================
   CONTENT CARDS
   =============================== */

.bill-box {
    padding: 25px;
    border-radius: 18px;

    background: rgba(255, 255, 255, 0.88);

    border: 1px solid rgba(255, 255, 255, 0.8);

    box-shadow:
        0px 10px 35px rgba(0, 0, 0, 0.10),
        0px 2px 8px rgba(0, 0, 0, 0.05);

    backdrop-filter: blur(12px);

    margin-top: 20px;
}


/* ===============================
   TOTAL BOX
   =============================== */

.total-box {
    padding: 20px;
    border-radius: 15px;

    background:
        linear-gradient(
            135deg,
            #e8f5e9,
            #f1f8e9,
            #ffffff
        );

    border: 1px solid #c8e6c9;

    text-align: right;

    margin-top: 15px;

    box-shadow:
        0px 5px 18px rgba(76, 175, 80, 0.12);
}


/* ===============================
   INPUT BOXES
   =============================== */

div[data-baseweb="input"] {
    border-radius: 12px !important;
}

div[data-baseweb="select"] {
    border-radius: 12px !important;
}


/* ===============================
   BUTTON
   =============================== */

.stButton > button {
    border-radius: 12px;

    font-weight: 700;

    min-height: 48px;

    border: none;

    background:
        linear-gradient(
            90deg,
            #ff512f,
            #dd2476
        );

    color: white;

    box-shadow:
        0px 6px 18px rgba(221, 36, 118, 0.25);

    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0px 10px 25px rgba(221, 36, 118, 0.35);
}


/* ===============================
   SECTION HEADINGS
   =============================== */

h1, h2, h3 {
    color: #2d3436;
}


/* ===============================
   DIVIDERS
   =============================== */

hr {
    border: none;

    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            #dddddd,
            transparent
        );

    margin: 25px 0;
}


/* ===============================
   FOOTER
   =============================== */

.footer {
    text-align: center;

    color: #666666;

    margin-top: 35px;

    padding: 20px;

    font-size: 15px;
}


/* ===============================
   SUCCESS MESSAGE
   =============================== */

div[data-testid="stAlert"] {
    border-radius: 12px;
}


/* ===============================
   MOBILE RESPONSIVE
   =============================== */

@media (max-width: 768px) {

    .title {
        font-size: 30px;
    }

    .subtitle {
        font-size: 15px;
    }

    .bill-box {
        padding: 18px;
    }

    .total-box {
        padding: 15px;
    }

}

</style>
""", unsafe_allow_html=True)


# -------------------------------
# Restaurant Menu
# -------------------------------

menu = {
    "🍔 Veg Burger": 120,
    "🍕 Margherita Pizza": 250,
    "🍝 Pasta": 180,
    "🍟 French Fries": 100,
    "🥪 Veg Sandwich": 130,
    "🌮 Veg Tacos": 160,
    "🍚 Fried Rice": 150,
    "🥤 Cold Drink": 60,
    "☕ Coffee": 80,
    "🍨 Ice Cream": 90
}


# -------------------------------
# Header
# -------------------------------

st.markdown(
    '<div class="title">🍔 Restaurant Bill Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Select your favorite food items and generate your bill instantly!</div>',
    unsafe_allow_html=True
)


# -------------------------------
# Customer Details
# -------------------------------

st.subheader("👤 Customer Details")

col1, col2 = st.columns(2)

with col1:
    customer_name = st.text_input(
        "Customer Name",
        placeholder="Enter customer name"
    )

with col2:
    table_number = st.number_input(
        "Table Number",
        min_value=1,
        max_value=100,
        value=1,
        step=1
    )


st.divider()


# -------------------------------
# Food Selection
# -------------------------------

st.subheader("🍽️ Select Food Items")

selected_items = st.multiselect(
    "Choose the items you want:",
    list(menu.keys()),
    placeholder="Select food items"
)


# Store bill items
bill_items = []


# -------------------------------
# Quantity Selection
# -------------------------------

if selected_items:

    st.write("### 🔢 Select Quantity")

    for item in selected_items:

        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(f"**{item}** — ₹{menu[item]}")

        with col2:
            quantity = st.number_input(
                f"Quantity for {item}",
                min_value=1,
                max_value=20,
                value=1,
                step=1,
                key=f"quantity_{item}"
            )

        item_total = menu[item] * quantity

        bill_items.append({
            "item": item,
            "price": menu[item],
            "quantity": quantity,
            "total": item_total
        })


# -------------------------------
# Billing Options
# -------------------------------

st.divider()

st.subheader("💰 Billing Options")

col1, col2 = st.columns(2)

with col1:

    tax_percentage = st.number_input(
        "Tax (%)",
        min_value=0.0,
        max_value=30.0,
        value=5.0,
        step=0.5
    )

with col2:

    discount_percentage = st.number_input(
        "Discount (%)",
        min_value=0.0,
        max_value=50.0,
        value=0.0,
        step=1.0
    )


# -------------------------------
# Generate Bill
# -------------------------------

st.divider()

generate_bill = st.button(
    "🧾 Generate Bill",
    type="primary",
    use_container_width=True
)


if generate_bill:

    if not customer_name.strip():

        st.warning("⚠️ Please enter the customer name.")

    elif not selected_items:

        st.warning("⚠️ Please select at least one food item.")

    else:

        # Calculate subtotal
        subtotal = sum(item["total"] for item in bill_items)

        # Calculate discount
        discount_amount = subtotal * discount_percentage / 100

        # Amount after discount
        amount_after_discount = subtotal - discount_amount

        # Calculate tax
        tax_amount = amount_after_discount * tax_percentage / 100

        # Grand total
        grand_total = amount_after_discount + tax_amount

        # -------------------------------
        # Bill Display
        # -------------------------------

        st.markdown(
            '<div class="bill-box">',
            unsafe_allow_html=True
        )

        st.markdown("## 🧾 FINAL BILL")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Customer:** {customer_name}")
            st.write(f"**Table Number:** {table_number}")

        with col2:
            current_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
            st.write(f"**Date & Time:** {current_time}")

        st.divider()

        # Bill table
        st.write("### 🍽️ Order Details")

        header1, header2, header3, header4 = st.columns([4, 1, 1, 2])

        with header1:
            st.write("**Item**")

        with header2:
            st.write("**Qty**")

        with header3:
            st.write("**Price**")

        with header4:
            st.write("**Total**")

        for item in bill_items:

            col1, col2, col3, col4 = st.columns([4, 1, 1, 2])

            with col1:
                st.write(item["item"])

            with col2:
                st.write(item["quantity"])

            with col3:
                st.write(f"₹{item['price']:.2f}")

            with col4:
                st.write(f"₹{item['total']:.2f}")

        st.divider()

        # -------------------------------
        # Bill Summary
        # -------------------------------

        col1, col2 = st.columns([3, 1])

        with col2:

            st.write(f"**Subtotal:** ₹{subtotal:.2f}")

            st.write(
                f"**Discount ({discount_percentage:.1f}%):** "
                f"- ₹{discount_amount:.2f}"
            )

            st.write(
                f"**Tax ({tax_percentage:.1f}%):** "
                f"+ ₹{tax_amount:.2f}"
            )

            st.markdown(
                f"""
                <div class="total-box">
                    <h2>Grand Total</h2>
                    <h1>₹{grand_total:.2f}</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

        st.success("✅ Bill generated successfully!")

        st.balloons()


# -------------------------------
# Footer
# -------------------------------

st.markdown(
    """
    <div class="footer">
        🍔 Thank you for visiting our restaurant! <br>
        Have a wonderful day 😊
    </div>
    """,
    unsafe_allow_html=True
)
