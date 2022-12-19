
$(document).ready(function () {
    listing();
});

function listing() {
    $.ajax({
        type: 'GET',
        url: '/shop',
        data: {},
        success: function (response) {
            let rows = response['shops']
            for (let i = 0; i < rows.length; i++) {
                let product_price = rows[i]['product_price']
                let product_name = rows[i]['product_name']
                let product_img = rows[i]['product_img']

                let temp_html = `<div class="col">
                                <div class="card h-100">
                                    <img src="${product_img}"
                                        class="card-img-top">
                                    <div class="card-body">
                                        <h5 class="card-title">${product_name}</h5>
                                        <p class="card-text">${product_price}</p>
                                    </div>
                                </div>
                            </div>`
                $('#cards-box').append(temp_html)

            }

        }
    })
}



function open_box() {
    $('#post-box').show()
}
function close_box() {
    $('#post-box').hide()
}


function another_page() {
    let user = $('#name').val()
    window.location.href = `/anotherpage`

}

function login() {
    let name = $('#name').val()
    let address = $('#address').val()
    $.ajax({
        type: "GET",
        url: "/account",
        data: { name_give: name },

        success: function (response) {
            let rows = response['account']

            a = 0
            for (let i = 0; i < rows.length; i++) {
                let identity = rows[i]['identity']
                let password = rows[i]['password']

                if ((identity == name) & (password == address)) {
                    console.log('success')
                    a = 1
                } else {
                    console.log('fail')
                }
            }
            if (a == 1) {
                alert('Login success')
                another_page();
            } else {
                alert('Login fail')
            }

        }
    })

}

function search() {
    let product_search = $('#product_search').val()
    alert(`cannot found ${product_search}`)
}
function enterkey() {
    if (window.event.keyCode == 13) {
        login();
    }
}
function enterkey_search() {
    let product_search = $('#product_search').val()
    if (window.event.keyCode == 13) {
        alert(`cannot found ${product_search}`)
    }
}



$(document).ready(function () {


    $('#showPassword').on('click', function () {
        var passwordField = $('#address');


        var passwordFieldType = passwordField.attr('type');


        if (passwordFieldType == 'password') {
            passwordField.attr('type', 'text');

            $(this).val('Hide');
        } else {
            passwordField.attr('type', 'password');

            $(this).val('Show');
        }
    });
});
