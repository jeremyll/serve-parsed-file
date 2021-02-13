$(document).ready(function() {
    $('.parsed-data').DataTable();
    $('.stats').DataTable({
      "paging":   false,
      "ordering": false,
      "info":     false,
      "searching": false
    });
} );
