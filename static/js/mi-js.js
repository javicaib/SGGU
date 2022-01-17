function eliminar_estudiante(id) {


    Swal.fire({
        title: 'Seguro que quiere eliminar?',
        showCancelButton: true,
        confirmButtonText: 'Sí, Eliminar',
        cancelButtonText: 'No, Cancelar',


    }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
            window.location.href = 'del_estudiante/' + id

        }
    })

}