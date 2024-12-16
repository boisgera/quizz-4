import marimo

__generated_with = "0.9.16"
app = marimo.App(width="medium")


@app.cell
def __(mo):
    mo.md("""# Mines AP 2024-2025 Groupe 6 - Quizz 4""")
    return


@app.cell
def __(mo):
    mo.md("""## Question 1""")
    return


@app.cell(hide_code=True)
def __(mo):
    widget_1 = mo.ui.code_editor(
    value = 
    """ class Snake:
        ..."""    
    )

    comments_1 = mo.ui.text_area(debounce=False)

    mo.md(f'''
    Développez une classe `Snake` minimale assurant le comportement suivant :

    ```python
    >>> snake = Snake(body=[[15, 15], [16, 15], [17,15]], direction=[1, 0])
    >>> snake.body
    [[15, 15], [16, 15], [17,15]]
    >>> snake.direction
    [1, 0]
    ```

    Votre code:

    {widget_1}

    Commentaires:

    {comments_1}
    ''')
    return comments_1, widget_1


@app.cell
def __(mo):
    mo.md("""## Question 2""")
    return


@app.cell(hide_code=True)
def __(mo):
    widget_2 = mo.ui.code_editor(value='''\
    class Snake:
        ...
        def get_head(snake):
            ...\
    ''')

    comments_2 = mo.ui.text_area(debounce=False)

    mo.md(f'''
    Implémentez une méthode `get_head` 

    ```python
    class Snake:
        ...
        def get_head(snake):
            ...
    ```

    permettant l'usage suivant:

    ```python
    >>> snake = Snake(body=[[15, 15], [16, 15], [17,15]], direction=[1, 0])
    >>> snake.get_head()
    [17, 15]
    ```

    Votre réponse:
    {widget_2}

    Commentaires:

    {comments_2}
    ''')
    return comments_2, widget_2


@app.cell
def __(mo):
    mo.md("""## Question 3""")
    return


@app.cell(hide_code=True)
def __(mo):
    widget_3 = mo.ui.text(debounce=False, value="snake")
    comments_3 = mo.ui.text_area(debounce=False)

    mo.md(
        f"""\
    Dans la définition de la méthode `get_head`, le premier argument est nommé `snake`. 
    Conventionnellement en Python on lui donne un autre nom. Lequel ?

    {widget_3}

    Commentaires :

    {comments_3}

    """
    )
    return comments_3, widget_3


@app.cell(hide_code=True)
def __(mo):
    widget_4 = mo.ui.code_editor(value=
    """\
    class Snake:
        ...
        def move(...):
            ...\
    """)                             
    comments_4 = mo.ui.text_area(debounce=False)


    mo.md(f"""## Question 4

    Implémentez une méthode `move` de `Snake`

    {widget_4}

    def telle sorte que le serpent se comporte comme suit :

    ```pycon
    >>> snake = Snake(body=[[15, 15], [16, 15], [17,15]], direction=[1, 0])
    >>> snake.move()
    >>> snake.body
    [[16, 15], [17, 15], [18, 15]]
    >>> snake.direction
    [1, 0]
    >>> snake.move(direction=[0, 1])
    >>> snake.body
    [[17, 15], [18, 15], [18, 16]]
    >>> snake.direction
    [0, 1]
    >>> snake.move()
    >>> snake.body
    [[18, 15], [18, 16], [19, 16]]
    >>> snake.direction
    [0, 1]
    ```

    Commentaires :

    {comments_4}

    """)
    return comments_4, widget_4


@app.cell(hide_code=True)
def __(mo):
    widget_5 = mo.ui.array([mo.ui.checkbox()] * 4)
    comments_5 = mo.ui.text_area(debounce=False)


    mo.md(f"""## Question 5

    Sélectionnez les expressions alternatives valides pour déplacer le serpent :

     - {widget_5[0]} `Snake.move()`

     - {widget_5[1]} `Snake.move(direction=[1, 0])`

     - {widget_5[2]} `Snake.move(snake)`

     - {widget_5[3]} `Snake.move(snake, direction=[1, 0])`

    Commentaires :

    {comments_5}


    """)
    return comments_5, widget_5


@app.cell
def __(mo):
    widget_6 = mo.ui.code_editor(value='''\
    class Snake:
        ...\
    ''')

    comments_6 = mo.ui.text_area(debounce=False)

    mo.md(f'''

    Faites en sorte de modifier la classe `Snake` pour que l'on puisse imprimer les instance de serpent de la façon suivante :

    ```python
    >>> snake = Snake(body=[[15, 15], [16, 15], [17,15]], direction=[1, 0])
    >>> print(snake)
    Snake(body=[[15, 15], [16, 15], [17,15]], direction=[1, 0])
    ```



    Votre réponse:

    {widget_6}

    Commentaires :

    {comments_6}

    ''')
    return comments_6, widget_6


@app.cell
def __(mo):
    mo.md("""## Validation""")
    return


@app.cell(hide_code=True)
def __():
    import pprint
    import urllib
    return pprint, urllib


@app.cell(hide_code=True)
def __():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def __(
    comments_1,
    comments_2,
    comments_3,
    comments_4,
    comments_5,
    comments_6,
    pprint,
    widget_1,
    widget_2,
    widget_3,
    widget_4,
    widget_5,
    widget_6,
):
    widgets = [widget_1, widget_2, widget_3, widget_4, widget_5, widget_6]
    comments = [comments_1, comments_2, comments_3, comments_4, comments_5, comments_6]
    answer = pprint.pformat([
        {f"Question {i+1}": widget.value, f"Comment {i+1}": comment.value} for i, (widget, comment) in enumerate(zip(widgets, comments))
    ], indent=4)
    return answer, comments, widgets


@app.cell(hide_code=True)
def __(mo):
    autosave = mo.ui.checkbox(label="Sauvegarde automatique dans le fichier answer.py", value=True)
    autosave
    return (autosave,)


@app.cell(hide_code=True)
def __(answer, autosave):
    if autosave.value:
        with open("answer.py", mode="tw", encoding="utf-8") as file:
            file.write(answer)
    return (file,)


@app.cell(hide_code=True)
def __(answer, mo, urllib):
    to = "Sebastien.Boisgerault@minesparis.psl.eu"
    subject = "Quizz AP #3"
    body = answer

    q = urllib.parse.quote


    mailto = f"mailto:{to}?subject={q(subject)}&body={q(body)}"


    mo.vstack(
        [
            mo.md(f"""
    Envoyez le texte suivant à {mo.icon('lucide:mail')} `Sebastien.Boisgerault@minesparis.psl.eu`
    ```python
    {answer}
    ```
    """),
            mo.Html(f"""
    <div>
      <style>
        #send {{
          text-decoration: none;
          background-color: #EEEEEE;
          color: #333333;
          padding: 2px 6px 2px 6px;
          border-top: 1px solid #CCCCCC;
          border-right: 1px solid #333333;
          border-bottom: 1px solid #333333;
          border-left: 1px solid #CCCCCC;
        }}
        </style>
        <a id="send" href="{mailto}">Envoyez votre réponse</a>
    <div>
    """),
        ]
    )
    return body, mailto, q, subject, to


if __name__ == "__main__":
    app.run()
