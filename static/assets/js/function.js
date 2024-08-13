$(document).ready(function() {
    $('#commentForm').submit(function(e) {
        e.preventDefault();
        $.ajax({
            data: $(this).serialize(),
            method: $(this).attr("method"),
            url: $(this).attr("action"),
            dataType: "json",
            success: function(res) {
                console.log('AJAX Success:', res); // Debugging line
                if (res.bool === true) {
                    $("#review_res").html("Thank you for giving us your valuable review 😊");
                    $(".hide_comment_form").hide();
                    $(".add_review").hide();  
                    
                    let rating = res.context.rating;
                    let stars = '';
                    for (let i = 0; i < rating; i++) {
                        stars += '<i class="fas fa-star text-warning"></i>';
                    }
                    for (let i = rating; i < 5; i++) {
                        stars += '<i class="far fa-star text-warning"></i>';  // Optional: Empty stars
                    }

                    let _html = `
                        <div class="single-comment justify-content-between d-flex mb-30">
                            <div class="user justify-content-between d-flex">
                                <div class="thumb text-center">
                                    <img src="https://cdn-icons-png.flaticon.com/512/3607/3607444.png" alt=""/>
                                    <a href="#" class="font-heading text-brand">${res.context.username}</a>
                                </div>
                                <div class="desc">
                                    <div class="d-flex justify-content-between mb-10">
                                        <div class="d-flex align-items-center">
                                            <span class="font-xs text-muted">${new Date(res.context.date).toLocaleDateString("en-GB")}</span>
                                        </div>
                                        <div class="product-rate d-inline-block">
                                            ${stars}
                                        </div>
                                    </div>
                                    <p class="mb-10">${res.context.review}<a href="#" class="reply">Reply</a></p>
                                </div>
                            </div>
                        </div>`;

                    // Ensure the comment-list container exists
                    if ($(".comment-list").length) {
                        $(".comment-list").prepend(_html);
                    } else {
                        console.error('Container not found');
                    }
                } else {
                    console.error('Review submission failed:', res);
                }
            },
            error: function(xhr, status, error) {
                console.error('AJAX Error:', status, error);
            }
        });
    });
});


$(document).ready(function(){
    const $maxPrice = $("#max_price");

    $(".filter-checkbox, #price-filter-btn").on("click", function(){
        console.log("click");

        let filterobject = {};
        let min_price = parseFloat($maxPrice.attr("min"));
        let max_price = parseFloat($maxPrice.val());

        filterobject.min_price = min_price;
        filterobject.max_price = max_price;

        $(".filter-checkbox").each(function(){
            let filter_value = $(this).val();
            let filter_key = $(this).data("filter");
            filterobject[filter_key] = Array.from(document.querySelectorAll(`input[data-filter="${filter_key}"]:checked`))
                                          .map(element => element.value);
        });

        console.log("filter objects are: ", filterobject);

        $.ajax({
            url: '/filter-products',
            data: filterobject,
            dataType: 'json',
            beforeSend: function(){
                console.log("Sending Data......");
            },
            success: function(res){
                console.log(res);
                $("#filtered-product").html(res.data);
            },
            error: function(xhr, status, error) {
                console.error("AJAX Error: ", status, error);
            }
        });
    });

    // Price filter validation
    $maxPrice.on("blur", function() {
        let min_price = parseFloat($maxPrice.attr("min"));
        let max_price = parseFloat($maxPrice.attr("max"));
        let current_value = parseFloat($maxPrice.val());

        if(current_value < min_price || current_value > max_price){
            alert(`Make sure price is between ₹${min_price} and ₹${max_price}`);
            $(this).val(min_price);
            $("#range").val(min_price);
            $(this).focus();
            return false;
        }
    });
});


//-------add to cart funvtion--------

$("#add-to-cart-btn").on("click",function(){

    let this_val = $(this)
    let _index = this_val.attr("data-index")

    let quantity = $(".product-quantity-"+_index).val()
    let product_title = $(".product-title-"+_index).val()

    let product_id = $(".product-id-"+_index).val()
    let product_pid = $(".product-pid-"+_index).val()

    let product_image=$(".product-image-"+_index).val()
    let product_price = $(".current-price-"+_index).text()

    console.log("quantity: ",quantity);
    console.log("product_title: ",product_title);
    console.log("product_price: ",product_price);
    console.log("product_id: ",product_id);
    console.log("product_pid: ",product_pid);
    console.log("product_image: ",product_image);
 
    
    // $.ajax({
    //     url:"/add-to-cart",
    //     data:{
    //         "id":product_id,
    //         "qty":quantity,
    //         "title":product_title,
    //         "price":product_price
    //     },
    //     dataType:"json",
    //     beforeSend:function(){
    //         console.log("Adding product to cart");
    //     },
    //     success:function(res){
    //        this_val.html("Added to cart");
    //        $(".cart-items-count").text(res.totalcartitems)
           
    //     }
    // })
    

})




