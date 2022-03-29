msi_rtxa5000_price = 4199.35
gigabyte_aero_price = 4295.54
razer_blade15_price = 3696.99
asus_zephyrus_m16_price = 1849.79
amd_ryzen_9_5900HX_price = 1399.99
geforce_rtx_3050_price = 699.99

#msi_rtx = 
max_price = max(msi_rtxa5000_price, gigabyte_aero_price, razer_blade15_price, asus_zephyrus_m16_price, amd_ryzen_9_5900HX_price, geforce_rtx_3050_price)
print(f"The most expensive laptop price is ${max_price}.")

min_price = min(msi_rtxa5000_price, gigabyte_aero_price, razer_blade15_price, asus_zephyrus_m16_price, amd_ryzen_9_5900HX_price, geforce_rtx_3050_price)
print(f"The least expensive laptop price is ${min_price}.")

# rounded_price = round(msi_rtxa5000_price, gigabyte_aero_price, razer_blade15_price, asus_zephyrus_m16_price, amd_ryzen_9_5900HX_price, geforce_rtx_3050_price)
rounded_price = round(msi_rtxa5000_price, 1)
print(f"The rounded price of the MSI RTX 5000 is ${rounded_price}.")
rounded_price = round(gigabyte_aero_price, 1)
print(f"The rounded price of the Gigabyte Areo is ${rounded_price}.")
rounded_price = round(razer_blade15_price, 1)
print(f"The rounded price of the Razer Blade is ${rounded_price}.")
rounded_price = round(asus_zephyrus_m16_price, 1)
print(f"The rounded price of the Asus Zephyrus is ${rounded_price}.")
rounded_price = round(amd_ryzen_9_5900HX_price, 1)
print(f"The rounded price of the AMD Ryzen 5900 is ${rounded_price}.")
rounded_price = round(geforce_rtx_3050_price, 1)
print(f"The rounded price of the GeForce RTX 3050 is ${rounded_price}.")