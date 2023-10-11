// add an item to cart
$('.plus-cart').click(function(){
    var itemID = $(this).attr("pid").toString();
    var el = this.parentNode.children[1];

    $.ajax({
        type: "GET",
        url: "/items/cart/",
        data: {
            "cart-item": itemID,
        },
        success:function(data) {
            el.innerText = data.quantity
            document.getElementById("total-cost").innerText = data.total_cost
            
            var itemCostElement = $(el).closest("tr").find("#item-cost-" + itemID);
            
            for (var i = 0; i <= data.item_cost.length; i++) {
                itemCostElement.text(data.item_cost[i]);
            }
        }
    })
})

// decrement quantity in cart
$('.minus-cart').click(function(){
    var itemID = $(this).attr("pid").toString();
    var el = this.parentNode.children[1];

    $.ajax({
        type: "GET",
        url: "/items/cart/",
        data: {
            "minus-cart-item": itemID,
        },
        success:function(data) {
            el.innerText = data.quantity
            document.getElementById("total-cost").innerText = data.total_cost
            
            var itemCostElement = $(el).closest("tr").find("#item-cost-" + itemID);
            
            for (var i = 0; i <= data.item_cost.length; i++) {
                itemCostElement.text(data.item_cost[i]);
            }
        }
    })
})

// remove an item from cart
$('.remove-cart').click(function () {
    var itemID = $(this).attr("pid").toString();
    var el = this
    $.ajax ({
        type: "GET",
        url: "/items/cart/",
        data: {
            "delete-cart-item": itemID
        },
        success:function(data) {
            document.getElementById("total-cost").innerText = data.total_cost
            el.parentNode.parentNode.remove()
        }
    })
    
})