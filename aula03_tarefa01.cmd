REM "Executar esse código na pasta que tem q criar o repositorio git"
git config --global user.name "Pedro Saint Martin"
git config --global user.email "teste@gmail.com"

mkdir projeto_python_uc1
cd projeto_python_uc1

git init

echo "Ola, Mundo !" > README.txt

git add README.txt
git commit README.txt -m "Primeiro commit"

git branch novaFuncionalidade
git checkout novaFuncionalidade

REM "Usando dois sinais de maior que adiciona linhas ao arquivo, se utilizar uma apaga-se tudo e cria um novo arquivo"
echo "Nova Funcionalidade" >> novaFuncionalidade.txt
echo "Nova Funcionalidade" >> novaFuncionalidade.txt
echo "Nova Funcionalidade" >> novaFuncionalidade.txt

echo "Nova Funcionalidade" > novaFuncionalidade.txt

git add .
git commit -m "Adicionar nova funcionalidade"

git checkout master
