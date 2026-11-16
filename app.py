
import streamlit as st
from datetime import date, datetime

st.set_page_config(page_title="Ghazi's Invoice Generator", page_icon="🧾")

st.title("🧾 Ghazi's Invoice Generator")
st.write("Create your invoice easily!")

invoice_type = st.radio(
    "Choose Invoice Type",
    ["Normal Invoice", "Grocery Invoice", "Grocery With Voucher Invoice"]
)

st.divider()

with st.form("invoice_form"):

    st.subheader("Invoice Details")

    heading = st.text_input("Invoice Heading")
    invoice_date = st.date_input("Date", value=date.today())
    invoice_time = st.time_input("Time", value=datetime.now().time())
    details = st.text_area("Additional Details")

    items = []
    subtotal = 0.0

    if invoice_type != "Normal Invoice":

        st.subheader("Grocery Items")

        for i in range(5):
            col1, col2 = st.columns(2)

            with col1:
                item = st.text_input(
                    f"Grocery Item {i+1}",
                    key=f"item_{i}"
                )

            with col2:
                price = st.number_input(
                    f"Price {i+1} (AED)",
                    min_value=0.0,
                    key=f"price_{i}"
                )

            if item.strip():
                items.append((item, price))
                subtotal += price

    discount = 0.0

    if invoice_type == "Grocery With Voucher Invoice":
        st.subheader("Voucher")
        discount = st.number_input(
            "Enter Voucher Discount (AED)",
            min_value=0.0
        )

    submitted = st.form_submit_button("Generate Invoice")

if submitted:

    st.divider()
    st.subheader("Your Invoice")

    st.write("**Heading:**", heading)
    st.write("**Date:**", invoice_date)
    st.write("**Time:**", invoice_time)
    st.write("**Details:**", details)

    if invoice_type == "Normal Invoice":

        st.success("Normal invoice generated!")

    else:

        tax = 1.0

        if discount > subtotal:
            st.error("Voucher cannot exceed the subtotal.")

        else:
            st.write("### Grocery Items")

            for item, price in items:
                st.write(f"{item} — AED {price:.2f}")

            total = subtotal + tax - discount

            st.write(f"**Subtotal:** AED {subtotal:.2f}")
            st.write(f"**Tax:** AED {tax:.2f}")

            if discount > 0:
                st.write(f"**Discount:** AED {discount:.2f}")

            st.subheader(f"Final Total: AED {total:.2f}")

            st.success("Invoice generated successfully!")

    st.write("Thank you for using Ghazi's Invoice Generator! ❤️")
