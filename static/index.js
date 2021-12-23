var app = angular.module('main', []);
app.controller('index', function ($scope, $http) {

    //VARIAVEIS

    $scope.dadosConsulta = "";
    /*$scope.dadosAlterar = {
        'id': '',
        'nome': '',
        'data': '',
        'sistema': '',
        'situacao': ''
    };*/
    $scope.dadosAlterar = [];
    $scope.dadosRelatorio = "";
    $scope.dadosSistema = "";
    $scope.idDeletar = "";
    $scope.mensagemConsulta = "";
    $scope.mensagemAlterar = "";
    $scope.mensagemDeletar = "";
    $scope.mensagemRelatorio = "";
    $scope.mensagemSistema = "";

    //FUNCOES

    $scope.consultar = function() {
        $http.get('/', {params: {dados: '*'}}).then(function (response) {
            $scope.dadosConsulta = response.data;
            $scope.mensagemConsulta = "Consulta realizada com sucesso!";
        }, function () {
            $scope.mensagemConsulta = "Ocorreu um erro! Contate o Administrador...";
        });
    };

    $scope.alterar = function(){
        $http.post('/', $scope.dadosAlterar).then(function (response) {
            if(response.data === "0") {
                $scope.mensagemAlterar = "Ocorreu um erro! Contate o Administrador...";
                return;
            }
            $scope.mensagemAlterar = "Alterado/Adicionado com sucesso!"
        }, function () {
            $scope.mensagemAlterar = "Ocorreu um erro! Contate o Administrador...";
        });
    };

    $scope.deletar = function(){
        $http.delete('/', {params: {dados: $scope.idDeletar}}).then(function (response) {
            $scope.mensagemDeletar = "Deletado com sucesso!"
        }, function () {
            $scope.mensagemDeletar = "Ocorreu um erro! Contate o Administrador...";
        });
    };

    $scope.relatorio = function() {
        $http.get('/', {params: {dados: 'relatorio'}, responseType: 'blob'}).then(function (response) {
            srcFile = URL.createObjectURL(response.data);
            window.open(srcFile);
            $scope.mensagemRelatorio = "Relatório gerado com sucesso!"
        }, function () {
            $scope.mensagemRelatorio = "Ocorreu um erro! Contate o Administrador...";
        });
    };

    $scope.sistema = function() {
        $http.get('/', {params: {dados: 'sistema'}}).then(function (response) {
            $scope.dadosSistema = response.data;
            $scope.mensagemSistema = "Aprovações em andamento atualizadas com sucesso!"
        }, function () {
            $scope.mensagemSistema = "Ocorreu um erro! Contate o Administrador...";
        });
    };


}).config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('//').endSymbol('//');
});
