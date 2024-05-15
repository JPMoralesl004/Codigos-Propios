print("Bienvenido a mi programa convertidor de divisas extranjeras a euros")

cambio_libras_a_euros = 1.15
cambio_dolares_a_euros = 0.92
cambio_quetzal_a_euros = 0.12
cambio_yuan_a_euros = 0.13
cambio_yen_a_euros = 0.0059
cambio_rublo_a_euros = 0.010

quiere_cambiar_libras_a_euros = input("¿Quieres cambiar libras a euros? (S/N) ")
if quiere_cambiar_libras_a_euros.upper() == "S":
    libras = float(input("Introduce la cantidad de libras que quieras cambiar: "))
    euros = libras * cambio_libras_a_euros
    print("{} libras son {} euros".format(libras, euros))

quiere_cambiar_dolares_a_euros = input("¿Quieres cambiar dólares a euros? (S/N) ")
if quiere_cambiar_dolares_a_euros.upper() == "S":
    dolares = float(input("Introduce la cantidad de dólares que quieras cambiar: "))
    euros = dolares * cambio_dolares_a_euros
    print("{} dólares son {} euros".format(dolares, euros))



