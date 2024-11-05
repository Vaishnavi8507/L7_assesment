import streamlit as st
from main import FictionalChocoHouse  

# Initialize the Chocolate House Management System
choco_house = FictionalChocoHouse()

# Function to display all flavors
def display_flavors():
    flavors = choco_house.get_all_flavours()
    if flavors:
        for flavour in flavors:
            st.write(f"ID: {flavour[0]}, Name: {flavour[1]}, Description: {flavour[2]}, Seasonal: {flavour[3]}, Season: {flavour[4]}")
    else:
        st.write("No flavors found.")

# Function to display all ingredients
def display_ingredients():
    ingredients = choco_house.get_all_ingredients()
    if ingredients:
        for ingredient in ingredients:
            st.write(f"ID: {ingredient[0]}, Name: {ingredient[1]}, Quantity: {ingredient[2]}, Unit: {ingredient[3]}, Allergen Info: {ingredient[4]}")
    else:
        st.write("No ingredients found.")

# Streamlit App Layout
st.title("Fictional Chocolate House Management")

# Sidebar menu
option = st.sidebar.selectbox("Select an option", ["View Flavors", "Add Flavor", "Delete Flavor", "Manage Ingredients", "Customer Suggestions"])

# Flavor Management
if option == "View Flavors":
    display_flavors()

elif option == "Add Flavor":
    st.subheader("Add New Flavor")
    name = st.text_input("Flavor Name")
    description = st.text_area("Flavor Description")
    is_seasonal = st.checkbox("Is Seasonal?")
    season = st.text_input("Season (if applicable)")
    if st.button("Add Flavor"):
        choco_house.add_flavour(name, description, is_seasonal, season)
        st.success(f"Flavor '{name}' added successfully!")

elif option == "Delete Flavor":
    display_flavors()
    flavour_id = st.number_input("Enter the ID of the flavour to delete:", min_value=1, step=1)
    if st.button("Delete Flavor"):
        if choco_house.delete_flavour(flavour_id):
            st.success(f"Flavor with ID {flavour_id} deleted successfully!")
            display_flavors()
        else:
            st.error(f"Failed to delete Flavor with ID {flavour_id}")

# Ingredient Management
elif option == "Manage Ingredients":
    sub_option = st.radio("Select Ingredient Option", ["View Ingredients", "Add Ingredient", "Delete Ingredient", "Update Ingredient Quantity"])
    
    if sub_option == "View Ingredients":
        display_ingredients()

    elif sub_option == "Add Ingredient":
        st.subheader("Add New Ingredient")
        name = st.text_input("Ingredient Name")
        quantity = st.number_input("Quantity", min_value=0)
        unit = st.text_input("Unit")
        allergen_info = st.text_input("Allergen Information (optional)")
        if st.button("Add Ingredient"):
            choco_house.add_ingredient(name, quantity, unit, allergen_info)
            st.success(f"Ingredient '{name}' added successfully!")

    elif sub_option == "Delete Ingredient":
        display_ingredients()
        ingredient_id = st.number_input("Enter the ID of the ingredient to delete:", min_value=1, step=1)
        if st.button("Delete Ingredient"):
            if choco_house.delete_ingredient(ingredient_id):
                st.success(f"Ingredient with ID {ingredient_id} deleted successfully!")
                display_ingredients()
            else:
                st.error(f"Failed to delete Ingredient with ID {ingredient_id}")

    elif sub_option == "Update Ingredient Quantity":
        display_ingredients()
        ingredient_id = st.number_input("Enter the ID of the ingredient to update:", min_value=1, step=1)
        new_quantity = st.number_input("New Quantity", min_value=0)
        if st.button("Update Quantity"):
            if choco_house.update_ingredient_quantity(ingredient_id, new_quantity):
                st.success(f"Quantity for ingredient ID {ingredient_id} updated successfully!")
                display_ingredients()
            else:
                st.error(f"Failed to update quantity for ingredient ID {ingredient_id}")

# Customer Suggestions
elif option == "Customer Suggestions":
    st.subheader("Customer Suggestions")
    suggestions = choco_house.get_all_suggestions()
    if suggestions:
        for suggestion in suggestions:
            st.write(f"ID: {suggestion[0]}, Flavor Name: {suggestion[1]}, Description: {suggestion[2]}, Allergen Concerns: {suggestion[3]}")
    else:
        st.write("No suggestions found.")

    flavour_name = st.text_input("Flavor Name for Suggestion")
    description = st.text_area("Suggestion Description")
    allergen_concerns = st.text_input("Allergen Concerns (optional)")
    if st.button("Add Suggestion"):
        choco_house.add_suggestion(flavour_name, description, allergen_concerns)
        st.success(f"Suggestion for flavor '{flavour_name}' added successfully!")
