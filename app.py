# ADD_EXPENSE section

with st.form("adding"):

title = st.text_input("Expense Title")

amount = st.number_input("Amount", step=1)

category = st.selectbox(
    "Category", ["Food", "Travel", "Shopping", "Bills", "Entertainment"]
)

expense_date = st.date_input("Expense Date")

btn = st.form_submit_button("ADD EXPENSE")

if btn:

    new_data = {
        "title": title,
        "amount": amount,
        "category": category,
        "expense_date": str(expense_date)
    }

    res = rq.post(
        f"{server_loc}/add_expense",
        json=new_data
    )

    st.success(res.json()["message"])


# VIEW_EXPENSES section

elif opt == "VIEW_EXPENSES":

st.header("VIEW EXPENSES")

res = rq.get(f"{server_loc}/get_expenses")

data = res.json()["expenses"]

df = pd.DataFrame(data)

st.dataframe(df)


# DELETE_EXPENSE section

elif opt == "DELETE_EXPENSE":


st.header("DELETE EXPENSE")

expense_id = st.number_input(
    "Enter Expense ID",
    step=1
)

if st.button("DELETE"):

    res = rq.delete(
        f"{server_loc}/delete_expense/{expense_id}"
    )

    st.success(res.json()["message"])


# UPDATE_EXPENSE section

elif opt == "UPDATE_EXPENSE":


st.header("UPDATE EXPENSE")

expense_id = st.number_input(
    "Enter Expense ID",
    step=1
)

title = st.text_input("New Title")

amount = st.number_input(
    "New Amount",
    step=1
)

category = st.selectbox(
    "New Category",
    ["Food", "Travel", "Shopping", "Bills", "Entertainment"]
)

expense_date = st.date_input("New Expense Date")

if st.button("UPDATE"):

    update_data = {
        "title": title,
        "amount": amount,
        "category": category,
        "expense_date": str(expense_date)
    }

    res = rq.put(
        f"{server_loc}/update_expense/{expense_id}",
        json=update_data
    )

    st.success(res.json()["message"])

