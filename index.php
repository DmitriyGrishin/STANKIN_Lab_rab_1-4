<?
require_once "php/connect.php";
?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="../css/style.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
    <script src='https://unpkg.com/tesseract.js@v2.1.0/dist/tesseract.min.js'></script>
    <title>Лабораторные работы</title>
</head>

<body>
    <header>
        <h1 class="zagolovok1"> Лабораторные работы</a></h1>
        <h2 class="zagolovok2"> Разработчик - Гришин Д.А. ИДМ-20-01</h2>
    </header>

<main>
    <div class="content">
        <h3 class="zagolovok3">Реализация клиент-серверной архитектуры. Лабораторная работа №1,4</h3>
        <div class="content__forms">
            <form class="firstform" action="php/create.php" method="post">
                    <div class="form__leftright">
                        <div class="form__left">
                            <div>Фамилия</div>
                            <div>Имя</div>
                            <div>Группа</div>
                        </div>
                        <div class="form__right">
                            <div><input type="text" name="surname"></input></div>
                            <div><input type="text" name="name"></input></div>
                            <div><input type="text" name="grp"></input></div>
                        </div>
                    </div>
                <div class="pushbtn">
                    <button type="submit">Отправить данные</button>
                </div>
            </form>
            <form class="secondform" action="php/excel.php" method="post">
            <button type="submit">Excel</button>
            </form>
        </div>
        <h3 class="zagolovok3">Распознавание текста. Лабораторная работа №3</h3>
             <div class="content__tesseract">
             <select id="langs">
  <option value="rus" selected>Русский</option>
  <option value="eng">English</option>
</select>
           <input type="file" id="file"></input>
           <div class="workplace">
           <div class="render" id="log"></div>
            </div>
           <div class="tesseract__buttonsdown">
            <button type="button" id="start">Начать обработку</button>
            <button onclick="copytext('#log')" type="button">Скопировать</button>
            <button id="wordexport" type="button">Word</button>
           </div>
            </div>
        </div>
        <script>

// Tesseract-OCR
            function recognize(file, lang, logger) {
  return Tesseract.recognize(file, lang, {logger})
   .then(({ data: {text }}) => {
     return text;
   })
}

const log = document.getElementById('log');

function updateProgress(data) {
  log.innerHTML = '';
  const statusText = document.createTextNode(data.status);
  const progress = document.createElement('progress');
  progress.max = 1;
  progress.value = data.progress;
  log.appendChild(statusText);
  log.appendChild(progress);
}

function setResult(text) {
  log.innerHTML = '';
  text = text.replace(/\n\s*\n/g, '\n');
  const pre = document.createElement('pre');
  pre.innerHTML = text;
  log.appendChild(pre);
}

document.getElementById('start').addEventListener('click', () => {
  const file = document.getElementById('file').files[0];
  if (!file) return;

  const lang = document.getElementById('langs').value;

  recognize(file, lang, updateProgress)
    .then(setResult);
});

// J-Query-Button-CopyText
function copytext(el) {
    var $tmp = $("<textarea>");
    $("body").append($tmp);
    $tmp.val($(el).text()).select();
    document.execCommand("copy");
    $tmp.remove();
}
        </script>
</main>

    <footer>

    </footer>

</body>

</html>
