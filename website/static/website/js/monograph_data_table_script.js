$(document).ready(function(){
    $('#monograph_table').DataTable({
        "lengthMenu": [ 15, 25, 50, 75, 100 ],
        "language": {
            "lengthMenu": "Mostrar _MENU_ monografías por página",
            "zeroRecords": "Nothing found - sorry",
            "info": "Mostrando página _PAGE_ de _PAGES_",
            "infoEmpty": "No records available",
            "infoFiltered": "(filtradas de _MAX_ monografías)",
            "search": "Buscar:",
            "paginate": {
                "first": "Primera",
                "last": "Ultima",
                "next": "Siguiente",
                "previous": "Anterior"
             }
        }
    });
    // $('#ex1').modal('show');
});