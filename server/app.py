from student_results_system.server import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=8008, debug=True)
    # python -m student_results_system.server.app

    # username, password, - username - student_no
    # reg-no, firtname, lastName, email

    # Login - useraname, password 
    # registration course, year, semister, course units(codes)
    # enroll, conituining , fresher, finalist,
    # see's his data with results if present
    # generates reg_permit, exmanation_permt, 
    # pays tution

    # dashboard - admin
    # enters courses and their units
    # enters results, views them
    # access using id, reg

    #