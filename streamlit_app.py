# Crear la ventana principal
root = tk.Tk()
root.title("Extractor de ID de Notion")

# Crear la caja de texto para pegar el enlace
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Botón para extraer el ID
extract_button = tk.Button(root, text="Extraer ID", command=extract_notion_id)
extract_button.pack(pady=5)

# Etiqueta para mostrar el ID extraído
id_label = tk.Label(root, text="")
id_label.pack(pady=5)

# Ejecutar la ventana
root.mainloop()
