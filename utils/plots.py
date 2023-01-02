import matplotlib.pyplot as plt



# Plota um gráfico de pizza com o valor absoluto e a porcentagem de cada valor da coluna.
def plotar_pizza(df, coluna):
    valores = df[coluna].value_counts()
    total = sum(valores)

    plt.pie(valores, labels=valores.index, autopct=lambda x: f'{x:.1f}%')
    plt.title(f'{coluna}: distribuição (%)', y=1.1)
    plt.show()


#  plotar histograma com porcentagem e valor absoluto
def plotar_barras_com_porcentagem(df, coluna):
    valores = df[coluna].value_counts()
    total = sum(valores)

    fig, ax = plt.subplots()
    ax.bar(valores.index, valores)
    ax.set_title(f'{coluna}: valor absoluto e porcentagem')

    for i, v in enumerate(valores):
        ax.text(i, v, f'{v} ({v/total:.1%})', ha='center')

    plt.show()
