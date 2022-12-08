from priorityData import main

import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Algortimo de prioridad")
size = "1150x500"
size_out = "1000x400"
root.config(bg='#49A')
root.geometry(size)

def algo(window, algorithm, queue, extra):
    def show_output(algorithm, output):
        def ret():
            top_out.grid_forget()
            label.grid_forget()
            button.grid_forget()
            output_win.destroy()

        output_win = tk.Toplevel()
        output_win.geometry(size)
        button = tk.Button(output_win, text="Salir", command=ret, height=2, width=14)

        wait_time = output[0]
        response_time = output[1]


        out = f"Tiempo promedio de espera: {round(wait_time,1)}\n\nTiempo promedio de retorno: {round(response_time,1)}\n\n"
        label = tk.Label(output_win, text=out, justify="left", font=("Times New Roman", 12, "normal"))
        top_out = tk.Label(output_win, text=f"Algoritmo seleccionado\n({algorithm})", font=("Times New Roman", 15, "normal"))
        t1 = tk.Label(output_win, text="Process ID", font=("Times New Roman", 15, "normal"))
        t2 = tk.Label(output_win, text="Burst Time", font=("Times New Roman", 15, "normal"))
        t3 = tk.Label(output_win, text="Arrival Time", font=("Times New Roman", 15, "normal"))
        t4 = tk.Label(output_win, text="Prioridad", font=("Times New Roman", 15, "normal"))
        tk.Label(output_win, text="  ").grid(row=0, column=0, padx=60)
        t1.grid(row=0, column=1, padx=60, pady=20)
        t2.grid(row=0, column=2, pady=20)
        t3.grid(row=0, column=3, padx=60, pady=20)
        t4.grid(row=0, column=4, padx=60)

        pri = [process[0] for process in queue]
        burst = [process[1] for process in queue]
        arriv = [process[2] for process in queue]

        for i in range(len(pri)):
            tk.Label(output_win, text=pri[i], font=("Times New Roman", 12, "normal")).grid(row=1+i, column=1)
            tk.Label(output_win, text=burst[i], font=("Times New Roman", 12, "normal")).grid(row=1+i, column=2)
            tk.Label(output_win, text=arriv[i], font=("Times New Roman", 12, "normal")).grid(row=1+i, column=3)
            tk.Label(output_win, text=Prioridad[i], font=("Times New Roman", 12, "normal")).grid(row=1 + i, column=4)

        top_out.grid(row=10, column=1, padx=60, pady=10)
        label.grid(row=11, column=1, padx=60)
        button.grid(row=12, column=2, sticky=tk.NSEW)
    if algorithm == "Non Preemption Priority ":
        Prioridad = []
        for idx in extra:
            try:
                value = int(idx.get())
            except:
                messagebox.showerror("¡Prioridades no válidas encontradas!", "Una o más prioridades no son números enteros.")
                return
            if not value:
                messagebox.showerror("¡Prioridades no válidas encontradas!", "Una o más prioridades están en blanco.")
                return
            Prioridad.append(value)
        output = main(queue, Prioridad)
        queue = output[2]

    elif algorithm == "Preemption Priority ":
        Prioridad = []
        for idx in extra:
            try:
                value = int(idx.get())
            except:
                messagebox.showerror("¡Prioridades no válidas encontradas!", "Una o más prioridades no son números enteros.")
                return
            if not value:
                messagebox.showerror("¡Prioridades no válidas encontradas!", "Una o más prioridades están en blanco.")
                return
            Prioridad.append(value)

        output = output = main(queue, Prioridad)
    else:
        messagebox.showerror("¡Seleccione el algoritmo primero! ",
                             "Haga clic en el botón Seleccionar algoritmo antes de enviar.")
        return
    show_output(algorithm, output)


def goto_submission(second, queue):
    global submit
    global extra
    submit = None
    extra = None
    third = tk.Toplevel()
    second.withdraw()
    third.config(bg='#49A')
    third.geometry(size)
    ids = [pri[0] for pri in queue]
    ids_stat = tk.Label(third, text=f"Process IDs: {ids}", relief=tk.SUNKEN, bd=2)
    sl = tk.Scale(third, from_=1, to=7, orient=tk.HORIZONTAL)
    pr = [process[0] for process in queue]
    pr_pris = [0 for i in pr]
    pr_idx = [0 for i in pr]
    pr_title = tk.Label(third, text="Process ID:")
    pris_title = tk.Label(third, text="Prioridad:")
    time_quantum = tk.Label(third, text="Priority")
    feedback_label = tk.Label(third, text="Threshold (integer in range 1-5):")
    feedback_threshold = tk.Entry(third)
    for i in range(len(pr)):
        pr_idx[i] = tk.Label(third, text=pr[i])
        pr_pris[i] = tk.Entry(third)

    multi_algos = [[
        ("Non Preemption Priority  with Prioryti: 2"),
        ("Non Preemption Priority  with Prioryti: 3"),
        ("Non Preemption Priority  with Prioryti: 4")
    ],[
        ("Non Preemption Priority  with Prioryti: 2"),
        ("Non Preemption Priority  with Prioryti: 3"),
        ("Non Preemption Priority  with Prioryti: 4"),
    ], [
        ("Preemption Priority  with Prioryti: 2"),
    ]]


    multi_level_algo_labels = []
    multi_level_algo_menus = []
    multi_level_algorithms = []
    multi_level_pr_labels = []
    multi_level_processes = []
    for level in range(3):
        multi_level_algo_labels.append(tk.Label(third, text=f"Level {level+1} Algorithm:"))
        multi_level_pr_labels.append(tk.Label(third, text=f"Process IDs for {level+1} Level (separated by ','): "))
        multi_level_algorithms.append(tk.StringVar())
        multi_level_algorithms[level].set(multi_algos[level][0])
        multi_level_algo_menus.append(tk.OptionMenu(third, multi_level_algorithms[level], *multi_algos[level]))
        multi_level_processes.append(tk.Entry(third))

    def select_algo(algorithm):
        global submit
        global extra
        extra = None
        lab.config(text=op.get())
        def clear():
            sl.grid_forget()
            feedback_threshold.grid_forget()
            feedback_label.grid_forget()
            time_quantum.grid_forget()
            pr_title.grid_forget()
            pris_title.grid_forget()
            for i in range(len(pr)):
                pr_idx[i].grid_forget()
                pr_pris[i].grid_forget()
            for level in range(3):
                    multi_level_algo_labels[level].grid_forget()
                    multi_level_algo_menus[level].grid_forget()
                    multi_level_pr_labels[level].grid_forget()
                    multi_level_processes[level].grid_forget()
        clear()
        if algorithm == "Non Preemption Priority " or algorithm == "Preemption Priority ":
            pr_title.grid(row=19, column=0)
            pris_title.grid(row=19, column=2)
            for i in range(len(pr)):
                pr_pris[i].delete(0, tk.END)
                pr_idx[i].grid(row=20+i, column=0)
                pr_pris[i].grid(row=20+i, column=2)
            extra = pr_pris
        submit = algorithm
    lab = tk.Label(third)
    modes = [
        ("Non Preemption Priority "),
        ("Preemption Priority "),
    ]
    op = tk.StringVar()
    op.set("Preemption Priority")
    option = tk.OptionMenu(third, op, *modes)
    b = tk.Button(third, text="Seleccionar algoritmo", height=2, width=30, command=lambda: select_algo(op.get()))
    b1 = tk.Button(third, text="Volver al inicio", height=2, width=30, command=lambda:goto_main(third))
    b2 = tk.Button(third, text="Enviar para procesar", height=2, width=30, command=lambda:algo(third, submit, queue, extra))
    option.config(height=1, width=40)
    option.grid(row=1, column=1, padx=60, pady=40)
    b.grid(row=2, column=1, padx=60, pady=30, sticky=tk.NSEW)
    b1.grid(row=2, column=0, padx=60, pady=30, sticky=tk.NSEW)
    b2.grid(row=2, column=2, padx=60, pady=30, sticky=tk.NSEW)
    lab.grid(row=3, column=1)
    ids_stat.grid(row=0, column=0, columnspan=3, padx=90, sticky=tk.W+tk.E)

def goto_random_queue():
    second = tk.Toplevel()
    root.withdraw()
    second.geometry(size)
    def generate_random_queue(length):
            queue = []
            choices = list(range(0,10))
            row1 = 2
            random.shuffle(choices)
            for i in range(length):
                pid = choices.pop()
                burst_time = random.randint(1, 10)
                arr_time = random.randint(0, 10)
                m1 = tk.Label(second, text=pid, font=("Times New Roman", 18, "normal"))
                m2 = tk.Label(second, text=burst_time, font=("Times New Roman", 18, "normal"))
                m3 = tk.Label(second, text=arr_time, font=("Times New Roman", 18, "normal"))
                m1.grid(row=row1, column=0)
                m2.grid(row=row1, column=1)
                m3.grid(row=row1, column=2)
                row1+=1
                queue.append((pid, burst_time, arr_time))
            return queue
    random_queue = generate_random_queue(length=4)
    v = tk.Label(second, text="Your Queue is:", font=("New Times Roman", 25, "normal"))
    value1 = tk.Label(second, text="Process ID", font=("Times New Roman", 15, "normal")).grid(row=1, column=0)
    value2 = tk.Label(second, text="Burst Time", font=("Times New Roman", 15, "normal")).grid(row=1, column=1)
    value3 = tk.Label(second, text="Arrival Time", font=("Times New Roman", 15, "normal")).grid(row=1, column=2)
    b1 = tk.Button(second, text="Volver al inicio", height=2, width=18, command=lambda: goto_main(second))
    b2 = tk.Button(second, text="Enviar", height=2, width=18, command=lambda: goto_submission(second, random_queue))
    v.grid(row=0, column=0, pady=40, padx=250, columnspan=3)
    b1.grid(row=8, column=0, sticky=tk.NSEW, padx=200, pady=70)
    b2.grid(row=8, column=2, sticky=tk.NSEW, padx=200, pady=70)

def goto_main(second):
    root.deiconify()
    second.withdraw()


def goto_user_queue():
    second = tk.Toplevel()
    second.config(bg='#49A')
    second.geometry(size)
    root.withdraw()
    e1 = tk.Entry(second)
    e2 = tk.Entry(second)
    e3 = tk.Entry(second)
    lab1 = tk.Label(second, text="Process ID:", font=("New Times Roman", 20, "normal"))
    lab2 = tk.Label(second, text="Burst Time:", font=("New Times Roman", 20, "normal"))
    lab3 = tk.Label(second, text="Arrival Time:", font=("New Times Roman", 20, "normal"))

    e1.grid(row=1, column=0, padx=115, pady=10, ipady=4, ipadx=2)
    e2.grid(row=1, column=1, padx=115, pady=10, ipady=4, ipadx=2)
    e3.grid(row=1, column=2, padx=115, pady=10, ipady=4, ipadx=2)
    lab1.grid(row=0, column=0, padx=30, pady=30)
    lab2.grid(row=0, column=1, padx=20, pady=30)
    lab3.grid(row=0, column=2, padx=30, pady=30)

    global row
    row = 30
    global count
    count = 0
    queue = []
    def give_row():
        global row
        row += 1
        return row
    def add_process():
        global count
        count += 1
        try:
            pid = int(e1.get())
            burst_time = int(e2.get())
            arr_time = int(e3.get())
        except:
            messagebox.showerror("¡Entrada no válida!", "Una o más entradas no son números enteros. Vuelva a intentarlo")
            return
        user_process = (pid, burst_time, arr_time)
        for pr in queue:
            if user_process[0] == pr[0]:
                messagebox.showerror("¡Los ID de proceso deben ser únicos!", "Ingresó un ID de proceso que no es único")
                e1.delete(0, tk.END)
                return
        if len(queue) > 6:
            messagebox.showwarning("¡Se alcanzó el máximo de entradas!", "El usuario puede ingresar un máximo de 7 procesos.")
            return
        row1 = give_row()
        if count == 1:
            lab4 = tk.Label(second, text="Process ID", font=("New Times Roman", 10, "normal"))
            lab5 = tk.Label(second, text="Burst Time", font=("New Times Roman", 10, "normal"))
            lab6 = tk.Label(second, text="Arrival Time", font=("New Times Roman", 10, "normal"))
            lab4.grid(row=3, column=0, padx=30, pady=10)
            lab5.grid(row=3, column=1, padx=20, pady=10)
            lab6.grid(row=3, column=2, padx=30, pady=10)
        value1 = tk.Label(second, text = pid, font=("Times New Roman", 15, "normal")).grid(row=row1, column=0,)
        value2 = tk.Label(second, text=burst_time, font=("Times New Roman", 15, "normal")).grid(row=row1, column=1)
        value3 = tk.Label(second, text=arr_time, font=("Times New Roman", 15, "normal")).grid(row=row1, column=2)
        queue.append(user_process)
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
    count=0
    b1 = tk.Button(second, text="Volver al inicio", height=2, command=lambda:goto_main(second))
    b2 = tk.Button(second, text="Agregar proceso", height=2,  command=add_process)
    b3 = tk.Button(second, text="Enviar", height=2, command=lambda:goto_submission(second, queue))
    b1.grid(row=2, column=0, padx=50, pady=50, sticky=tk.NSEW)
    b2.grid(row=2, column=1, padx=50, pady=50, sticky=tk.NSEW)
    b3.grid(row=2, column=2, padx=50, pady=50, sticky=tk.NSEW)



def goto_info():
    def cpu_scheduling_terms():
        sche = tk.Toplevel()
        sche.config(bg='#49A')
        sche.geometry(size)
        #--------------------------------------------------cpuexchange
        l1 = tk.Label(sche, text="Algoritmo de prioridad", font=("Times New Roman", 20, "bold"))
        t1 = "Cada proceso en la cola de procesos listos tiene una ID de proceso única, mediante la cual se identifica."
        t2 = "La hora a la que el proceso se envía a la cola de espera."
        t3 = "El tiempo mínimo requerido por el proceso para su finalización."
        t4 = "Es la prioridad de asignada a cada proceso"
        t5 = "El número máximo de veces que se puede ejecutar un proceso en una cola de alta prioridad antes de que su\n prioridad disminuya en una cola de comentarios de varios niveles."
        l2 = tk.Label(sche, text=t1, justify="left", font=("roboto", 11, "normal"))
        l3 = tk.Label(sche, text=t2, justify="left", font=("roboto", 11, "normal"))
        l4 = tk.Label(sche, text=t3, justify="left", font=("roboto", 11, "normal"))
        l5 = tk.Label(sche, text=t4, justify="left", font=("roboto", 11, "normal"))
        l6 = tk.Label(sche, text=t5, justify="left", font=("roboto", 11, "normal"))
        l1.grid(row=1, column=1, padx=50, pady=30, columnspan=2)
        tk.Label(sche, text=" ",).grid(row=0, column=0, padx=40)
        tk.Label(sche, text="Process Id:", font=("Times New Roman", 12, "bold")).grid(row=2, column=1, padx=5, sticky=tk.W)
        tk.Label(sche, text="Arrival Time:", font=("Times New Roman", 12, "bold")).grid(row=3, column=1, padx=5, sticky=tk.W)
        tk.Label(sche, text="Burst Time:", font=("Times New Roman", 12, "bold")).grid(row=4, column=1, padx=5, sticky=tk.W)
        tk.Label(sche, text="Priority:", font=("Times New Roman", 12, "bold")).grid(row=5, column=1, padx=5, sticky=tk.W)
        tk.Label(sche, text="Threshhold:", font=("Times New Roman", 12, "bold")).grid(row=6, column=1, padx=5, sticky=tk.W)
        l2.grid(row=2, column=2, pady=10, sticky=tk.W)
        l3.grid(row=3, column=2, pady=10, sticky=tk.W)
        l4.grid(row=4, column=2, pady=10, sticky=tk.W)
        l5.grid(row=5, column=2, pady=10, sticky=tk.W)
        l6.grid(row=6, column=2, pady=10, sticky=tk.W)

    # output parametres
    def output_parameters():
         para = tk.Toplevel()
         para.config(bg='#49A')
         para.geometry(size)
         m1 = tk.Label(para, text="Colaboradores", font=("Times New Roman", 20, "bold"))
         z1 = "Xavier Chavez"
         z2 = "Lilibeth Puchaicela"
         z3 = "Nixon Vuele"
         z4 = "Kriss Bustamante"

         m2 = tk.Label(para, text=z1, justify="left", font=("roboto", 11, "normal"))
         m3 = tk.Label(para, text=z2, justify="left", font=("roboto", 11, "normal"))
         m4 = tk.Label(para, text=z3, justify="left", font=("roboto", 11, "normal"))
         m5 = tk.Label(para, text=z4, justify="left", font=("roboto", 11, "normal"))

         m1.grid(row=1, column=1, padx=160, pady=50, columnspan=2)
         tk.Label(para, text=" ", ).grid(row=0, column=0, padx=175)
         tk.Label(para, text="xavierchavez916 ", font=("Times New Roman", 12, "bold")).grid(row=2, column=1, pady=10, padx=10, sticky=tk.W+tk.N)
         tk.Label(para, text="llpuchaicela ", font=("Times New Roman", 12, "bold")).grid(row=3, column=1, pady=10, padx=10,sticky=tk.W+tk.N)
         tk.Label(para, text="krissbustamante ", font=("Times New Roman", 12, "bold")).grid(row=4, column=1, pady=10, padx=10, sticky=tk.W+tk.N)
         tk.Label(para, text="NixonVuele" , font=("Times New Roman", 12, "bold")).grid(row=5, column=1, padx=10, pady=10, sticky=tk.W+tk.N)


         m2.grid(row=2, column=2, pady=10, sticky=tk.W+tk.N)
         m3.grid(row=3, column=2, pady=10, sticky=tk.W+tk.N)
         m4.grid(row=4, column=2, pady=10, sticky=tk.W+tk.N)
         m5.grid(row=5, column=2, pady=10, sticky=tk.W+tk.N)

    info = tk.Toplevel()
    info.config(bg='#49A')
    info.geometry(size)
    root.withdraw()
    r = tk.Label(info, text="Sobre el Algoritmo de prioridad", font=("Times New Roman", 25, "bold"))
    a = tk.Label(info, text="Algoritmo de Prioridad", font=("Times New Roman", 16, "bold"))
    aim = "Nuestro proyecto es una aplicación GUI basada en Tkinter que proporciona una interfaz dinámica e interactiva\n que nos permite realizar simulaciones del algoritmo de prioridad de CPU."
    l = tk.Label(info, text="En que consiste el algoritmo de prioridad", font=("Times New Roman", 16, "bold"))
    cpu = "Cada proceso tiene una prioridad, entrará primero en la CPU, el que tenga mayor prioridad.\n• Política de prioridades expulsiva o no.\n• La prioridad se puede definir\n• De forma interna, la define el SO.\n• De forma externa, la definen los usuarios.\n• Los procesos de prioridad más baja tienen riesgo de inanición."
    a1 = tk.Label(info, text=aim, justify="left", font=("roboto", 13, "normal"))
    a2 = tk.Label(info, text=cpu, justify="left", font=("roboto", 13, "normal"))

    r.grid(row=0, column=1, pady=20, columnspan=5)
    a.grid(row=1, column=1, pady=20, sticky=tk.W)
    l.grid(row=3, column=1, pady=20, sticky=tk.W, columnspan=2)
    a1.grid(row=2, column=1, sticky=tk.W, columnspan=5)
    a2.grid(row=4, column=1, sticky=tk.W, columnspan=5)
    tk.Label(info, text="  ").grid(row=0, column=0, padx=90)


    b1 = tk.Button(info, text="Volver a Inicio", height=2, width=20, command=lambda: goto_main(info))
    b2 = tk.Button(info, text="Terminos que necesitas conocer", height=2, width=20, command=cpu_scheduling_terms)
    b3 = tk.Button(root, text="Salir", height=2, command=root.quit)
    b4 = tk.Button(info, text="Colaboradores", height=2, width=20, command=output_parameters)

    b1.grid(row=6, column=1, padx=20, pady=40, sticky=tk.NSEW)
    b2.grid(row=6, column=2, padx=20, pady=40, sticky=tk.NSEW)
    b3.grid(row=6, column=3, padx=20, pady=40, sticky=tk.NSEW)
    b4.grid(row=6, column=4, padx=20, pady=40, sticky=tk.NSEW)


w = tk.Label(root, text = "Proyecto de Sistemas Operativos", font=('Times New Roman', 20 ,'normal'))
b1 = tk.Button(root, text="Generar procesos aleatoriamente", height=3, command=goto_random_queue)
b2 = tk.Button(root, text="Ingresar procesos", height=3, command=goto_user_queue)
b5 = tk.Button(root, text="Sobre el Algoritmo de Prioridad", height=3, command=goto_info)
b3 = tk.Button(root, text="Salir", height=3, command=root.quit)

w.grid(row=0, column=0, padx=400, pady=70, columnspan=3, sticky=tk.EW)
b1.grid(row=1, column=0, sticky=tk.NSEW, padx=20, pady=10)
b2.grid(row=1, column=1, sticky=tk.NSEW, padx=10, pady=10)
b3.grid(row=1, column=2, sticky=tk.NSEW, padx=20, pady=10)
b5.grid(row=2, column=0, sticky=tk.NSEW, padx=20, pady=10)
root.mainloop()
