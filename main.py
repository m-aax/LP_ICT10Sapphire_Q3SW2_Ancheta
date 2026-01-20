from pyscript import document, display #type: ignore

def get_team(event):
 
    medi = document.getElementById("medcert").value
    regi = document.getElementById("regis").value

    grade = document.getElementById("grade")
    section = document.getElementById("section")
    team_get = grade.value
    team_get2 = section.value

    # Determine Team Name
    if document.querySelector('input[name="regis"]:checked').value == "No" and document.querySelector('input[name="medcert"]:checked').value == "No":
        document.getElementById("team_name").innerText = ("Please continue your online registration and/or submit your medical certificate to join a team.")

    elif document.getElementById("grade").value == "g7":
        document.getElementById("team_name").innerText = "You are a Blue Bear!"
        document.getElementById("team_img").src = "bluebears.jpg"

    elif document.getElementById("grade").value == "g7":
        document.getElementById("team_name").innerText = "You are a Yellow Tiger!"
        document.getElementById("team_img").src = "YT.png"

    elif document.getElementById("grade").value == "g7":
        document.getElementById("team_name").innerText = "You are a Red Bulldog!"
        document.getElementById("team_img").src = "RB.png"

    elif document.getElementById("grade").value == "g7":
        document.getElementById("team_name").innerText = "You are a Green Hornet!"
        document.getElementById("team_img").src = "GH.png"

    elif document.getElementById("grade").value == "g8":
        document.getElementById("team_name").innerText = "You are a Red Bulldog!"
        document.getElementById("team_img").src = "RB.png"

    elif document.getElementById("grade").value == "g8":
        document.getElementById("team_name").innerText = "You are a Yellow Tiger!"
        document.getElementById("team_img").src = "YT.png"

    elif document.getElementById("grade").value == "g8":
        document.getElementById("team_name").innerText = "You are a Green Hornet!"
        document.getElementById("team_img").src = "GH.png"

    elif document.getElementById("grade").value == "g8"  :
        document.getElementById("team_name").innerText = "You are a Blue Bear!"
        document.getElementById("team_img").src = "bluebears.png"

    elif document.getElementById("grade").value == "g9"  :
        document.getElementById("team_name").innerText = "You are a Green Hornet!"
        document.getElementById("team_img").src = "GH.png"

    elif document.getElementById("grade").value == "g9"  :
        document.getElementById("team_name").innerText = "You are a Red Bulldog!"
        document.getElementById("team_img").src = "RB.png"

    elif document.getElementById("grade").value == "g9"  :
        document.getElementById("team_name").innerText = "You are a Blue Bear!"
        document.getElementById("team_img").src = "bluebears.png"

    elif document.getElementById("grade").value == "g9"  :
        document.getElementById("team_name").innerText = "You are a Yellow Tiger!"
        document.getElementById("team_img").src = "YT.png"

    elif document.getElementById("grade").value == "g10"  :
        document.getElementById("team_name").innerText = "You are a Yellow Tiger!"
        document.getElementById("team_img").src = "YT.png"

    elif document.getElementById("grade").value == "g10"  :
        document.getElementById("team_name").innerText = "You are a Blue Bear!"
        document.getElementById("team_img").src = "bluebears.png"

    elif document.getElementById("grade").value == "g10"  :
        document.getElementById("team_name").innerText = "You are a Green Hornet!!! You are also EXTREMELY GOATED (totally not baised)"
        document.getElementById("team_img").src = "GH.png"

    elif document.getElementById("grade").value == "g10"  :
        document.getElementById("team_name").innerText = "You are a Red Bulldog!"
        document.getElementById("team_img").src = "RB.png"

    else:
        document.getElementById("team_name").innerText = "You are a very super secret special case. Congradulations, but you have been chosen to be excempted from the intrams for being too unlucky or because I forgot how to fix my code"