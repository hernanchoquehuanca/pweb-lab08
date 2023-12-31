#!C:\xampp\perl\bin\perl.exe
use strict;
use warnings;
use CGI qw(standard);

my $q = CGI->new;
my $nc;
my $ng;
my $rp;
my $target = $q->param('op');

if(index($target,"+") != -1){
    $nc = substr($target, 0, index($target,"+"));
    $ng = substr($target,index($target,"+")+1);
    $rp = $nc+$ng;
}
if(index($target,"-") != -1){
    $nc = substr($target, 0, index($target,"-"));
    $ng = substr($target,index($target,"-")+1);
    $rp = $nc-$ng;
}
if(index($target,"*") != -1){
    $nc = substr($target, 0, index($target,"*"));
    $ng = substr($target,index($target,"*")+1);
    $rp = $nc*$ng;
}
if(index($target,"/") != -1){
    $nc = substr($target, 0, index($target,"/"));
    $ng = substr($target,index($target,"/")+1);
    $rp = $nc/$ng;
}


print $q->header('text/html');
print <<BLOCK;
<!DOCTYPE html>

<head>
    <meta charset="utf-8">
    <title>Calculadora</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../css/styles.css">
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            // Obtener el campo de entrada y los botones de la calculadora
            const operationInput = document.querySelector('.input-operation');
            const calculatorButtons = document.querySelectorAll('.calc-button');

            // Asignar un manejador de eventos a cada botón
            calculatorButtons.forEach(button => {
                button.addEventListener('click', function () {
                    // Agregar el valor del botón al campo de entrada
                    operationInput.value += button.textContent;
                });
            });
        });
    </script>
</head>

<body>
    <!-- contenido -->
    <div class="container">
        <h1>Calculadora utilizando expresiones regulares de perl</h1>
        <form action="calculadora.cgi" method="POST">
            <input type="text" name="op" value="$target" class="input-operation">
            <input type="text" name="rpta" value="$rp" class="input-operation">
            <div class="calculator-buttons">
                <table>
                    <tr>
                        <td><button type="button" class="calc-button">7</button></td>
                        <td><button type="button" class="calc-button">8</button></td>
                        <td><button type="button" class="calc-button">9</button></td>
                        <td><button type="button" class="calc-button operator">/</button></td>
                    </tr>
                    <tr>
                        <td><button type="button" class="calc-button">4</button></td>
                        <td><button type="button" class="calc-button">5</button></td>
                        <td><button type="button" class="calc-button">6</button></td>
                        <td><button type="button" class="calc-button operator">*</button></td>
                    </tr>
                    <tr>
                        <td><button type="button" class="calc-button">1</button></td>
                        <td><button type="button" class="calc-button">2</button></td>
                        <td><button type="button" class="calc-button">3</button></td>
                        <td><button type="button" class="calc-button operator">-</button></td>
                    </tr>
                    <tr>
                        <td><button type="button" class="calc-button">0</button></td>
                        <td><button type="button" class="calc-button">.</button></td>
                        <td><button type="submit" class="calc-button operator">=</button></td>
                        <td><button type="button" class="calc-button operator">+</button></td>
                    </tr>
                </table>
            </div>
            <input type="submit" value="Calcular" class="button">
            <input type="reset" value="Limpiar" class="button">
        </form>
    </div>
</body>
</html>
BLOCK

exit;