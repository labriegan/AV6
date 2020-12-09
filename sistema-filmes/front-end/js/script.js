$(function () {

  function showFilmes() {
    $.ajax({
      url: 'http://localhost:5000/get-filmes',
      method: 'GET',
      dataType: 'json', 
      success: listFilmes, 
      error: function () {
        alert('erro ao ler dados, verifique o backend');
      },
    });

    function listFilmes(filmes) {
      $("#tableBody").empty();
      showContent("container-listar");
      for (filme of filmes) {
        console.log(filme)
          var newRow = `<tr id="line_${filme.id}"> 
                          <td>${filme.nome}</td> 
                          <td>${filme.genero}</td> 
                          <td>${filme.distribuidora}</td> 
                          <td>${filme.diretores}</td>
                          <td>
                              <a href="#" id="delete_${filme.id}" class="delete_filme" title="Excluir filme">
                                  <span class="material-icons">
                                      delete
                                  </span>
                              </a>
                          </td>
                        </tr>`;
              $("#tableBody").append(newRow);
      }
    }
  }

  function showContent(nextPage) {
    $('#container-inicial').addClass('d-none');
    $('#container-listar').addClass('d-none');
    $("#tabela-reviews").addClass("d-none");
    $(`#${nextPage}`).removeClass('d-none');
  }

  $("#link-listar").click(function() {
    showFilmes();
  });

  $('#link-inicial').click(function () {
    showContent('container-inicial');
  });

  $('#nav-brand').click(function () {
    showContent('container-inicial');
  });

  $(document).on('click', '#btn-incluir', function () {
    const nome = $('#campo-nome').val();
    const genero = $('#campo-genero').val();
    const distribuidora = $('#campo-distribuidora').val();
    const diretores = $('#campo-diretores').val();

    const filmeData = JSON.stringify({
      nome: nome,
      genero: genero,
      distribuidora: distribuidora,
      diretores: diretores,
    
    });

    $.ajax({
      url: 'http://localhost:5000/create-filmes',
      type: 'POST',
      contentType: 'application/json',
      dataType: 'json',
      data: filmeData,
      success: createFilme,
      error: createFilmeError,
    });


    function createFilme(resposta) {
      if (resposta.result == 'ok') {
          $('#campo-nome').val('');
          $('#campo-genero').val('');
          $('#campo-distribuidora').val('');
          $('#campo-diretores').val('');
          alert('Filme adicionado com sucesso'); 
      } 
      else {
        alert(resposta.result + ':' + resposta.details);
      }
    };

    function createFilmeError(resposta){
      alert('Erro na chamada do back-end');
    }
  });

  $('#modal-incluir').on('hidden.bs.modal', function(e) {
    if (!$('#container-listar').hasClass('invisible')) {
        showFilmes();
    }
  });



  $(document).on("click", ".delete_filme", function() {
    var component = $(this).attr("id");

    var icon_name = "delete_";
    var filme_id = component.substring(icon_name.length);

    $.ajax({
      url: 'http://localhost:5000/delete-filmes/' + filme_id,
      type: "DELETE",
      dataType: "json",
      success: deletedFilme,
      error: deletedFilmeError
    });

    function deletedFilme(retorno) {
      if (retorno.result == "ok") {
          $('#line_' + filme_id).fadeOut(1000, function() {
              alert("Filme Removido com Sucesso!");
              showFilmes();
          });
      } 
      else {
          alert(`${retorno.result}: ${retorno.details}`);
      }
    }

      function deletedFilmeError(response) {
        alert("Erro ao excluir dados, verifique o Backend!");
  }});

    function listar_reviews() {
        $.ajax({
            url: 'http://localhost:5000//listar_reviews',
            method: 'GET',
            dataType: 'json',
            success: listar, 
            error: function(problema) {
                alert("erro ao ler dados, verifique o backend: ");
        }

    });
        function listar (reviews_cadastrados) {
            $('#corpoTabelaReviewsCadastrados').empty();
            showContent("tabela-reviews");       
            for (var i in reviews_cadastrados) { 
                lin = '<tr id="linha_review_'+reviews_cadastrados[i].id+'">' + 
                '<td>' + reviews_cadastrados[i].filme.nome + '</td>' + 
                '<td>' + reviews_cadastrados[i].nota + '</td>' +   
                '<td>' + reviews_cadastrados[i].espectador.nome + '</td>' +  
                '</tr>';
                $('#corpoTabelaReviewsCadastrados').append(lin);
            }
        }
    }

    $(document).on("click", "#linkListarReviewsCadastrados", function() {
        listar_reviews();
    });

  showContent("container-inicial");
});