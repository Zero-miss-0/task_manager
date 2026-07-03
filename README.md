[README.md](https://github.com/user-attachments/files/29645652/README.md)
# task_manager
This project is a terminal-based Project and Task Management application developed using Object-Oriented Programming (OOP) principles in Python.
# 📋 Task Manager — سیستم مدیریت پروژه و وظایف

> **Terminal-Based Project & Task Management System** built with Python and Object-Oriented Programming principles.

یک برنامه کنسولی برای مدیریت پروژه‌ها و وظایف، پیاده‌سازی‌شده با تمرکز بر اصول شیءگرایی در Python.

---

## 🎯 معرفی پروژه

این پروژه یک برنامه کنسولی (Terminal-Based Application) برای مدیریت پروژه‌ها و وظایف است که با استفاده از مفاهیم **شیءگرایی (Object-Oriented Programming)** در Python پیاده‌سازی شده.

هدف اصلی، نمایش کاربرد عملی مفاهیم زیر است:

- طراحی کلاس‌ها
- کپسوله‌سازی (Encapsulation)
- وراثت (Inheritance)
- چندریختی (Polymorphism)
- مدیریت خطا (Exception Handling)
- استفاده از Dunder Methods
- طراحی ماژولار (Modular Programming)

> تمام اطلاعات پروژه‌ها و وظایف تنها در حافظه (Memory) نگهداری می‌شوند و پس از خروج از برنامه ذخیره نمی‌شوند.

---

## 🛠 پیش‌نیازها (Requirements)

- Python 3.9 یا بالاتر

هیچ کتابخانه خارجی نیاز نیست — فقط با کتابخانه استاندارد پایتون کار می‌کنه.

---

## 📁 ساختار پروژه

```
task_manager/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── project.py
│   ├── task.py
│   ├── personal_task.py
│   ├── team_task.py
│   └── urgent_task.py
│
├── services/
│   ├── __init__.py
│   ├── manager.py
│   └── reports.py
│
├── exceptions/
│   ├── __init__.py
│   └── custom_errors.py
│
├── utils/
│   ├── __init__.py
│   └── validators.py
│
└── README.md
```

---

## ▶️ نحوه اجرای برنامه

```bash
git clone https://github.com/Zero-miss-0/task-manager.git
cd task-manager
python main.py
```

---

## 🧱 معرفی کلاس‌ها

### 1. کلاس `Project`

نماینده یک پروژه است.

**خصوصیات:** `project_id`, `name`, `description`

**وظایف:**
- نگهداری اطلاعات پروژه
- نمایش اطلاعات پروژه
- نگهداری لیست وظایف مربوط به پروژه
- محاسبه تعداد وظایف (با `__len__`)

### 2. کلاس `Task` (کلاس پایه)

تمام انواع وظایف از این کلاس ارث‌بری می‌کنند.

**خصوصیات:** `task_id`, `title`, `deadline`, `priority`, `status`, `project_id`

**ویژگی‌های مهم:** اعتبارسنجی وضعیت و اولویت، Getter/Setter، متد `calculate_score()`

### 3. کلاس `PersonalTask` *(ارث‌بر از Task)*

ویژگی اضافه: `owner_name`

```
score = priority × 10
```

### 4. کلاس `TeamTask` *(ارث‌بر از Task)*

ویژگی اضافه: `team_size`

```
score = priority × team_size
```

### 5. کلاس `UrgentTask` *(ارث‌بر از Task)*

ویژگی اضافه: `urgency_level`
محدودیت: اولویت فقط باید 4 یا 5 باشد.

```
score = priority × urgency_level × 5
```

### 6. کلاس `TaskManager`

مسئول مدیریت کل سیستم: افزودن/حذف/ویرایش پروژه و وظیفه، جستجو، تغییر وضعیت، تولید گزارش، مرتب‌سازی و نمایش آمار.

---

## 🌳 وراثت (Inheritance)

```
                Task
                  │
     ┌────────────┼────────────┐
     │            │            │
PersonalTask   TeamTask   UrgentTask
```

ویژگی‌های مشترک داخل کلاس `Task` قرار گرفته‌اند و کلاس‌های فرزند فقط ویژگی‌های مخصوص خود را اضافه می‌کنند.

---

## 🔄 چندریختی (Polymorphism)

هر کلاس فرزند نسخه مخصوص خودش را از متد `calculate_score()` پیاده‌سازی می‌کند:

```python
tasks = [
    PersonalTask(...),
    TeamTask(...),
    UrgentTask(...)
]

for task in tasks:
    print(task.calculate_score())
```

بدون نیاز به بررسی نوع شیء، متد مناسب هر کلاس اجرا می‌شود.

---

## 🔒 کپسوله‌سازی (Encapsulation)

در کلاس `Task` دو ویژگی به‌صورت private تعریف شده‌اند:

```python
__priority
__status
```

دسترسی فقط از طریق Getter/Setter انجام می‌شود:

```python
task.set_priority(4)
task.set_status("Completed")
```

Setterها مسئول اعتبارسنجی داده‌ها هستند.

---

## ⚠️ مدیریت خطاها (Exception Handling)

Exceptionهای سفارشی تعریف‌شده:

- `DuplicateIDError`
- `InvalidPriorityError`
- `InvalidStatusError`
- `EmptyStrParametersError`
- `ProjectNotFoundError`
- `TaskNotFoundError`
- `InvalidMenuChoiceError`

در صورت وقوع خطا، برنامه متوقف نمی‌شود و پیام مناسب نمایش داده می‌شود:

```
Error: Priority must be between 1 and 5.
```

---

## ✨ Dunder Methods استفاده‌شده

| متد | کاربرد |
|---|---|
| `__init__` | مقداردهی اولیه اشیا |
| `__str__` | نمایش خوانا برای کاربر |
| `__repr__` | نمایش فنی شیء |
| `__len__` | نمایش تعداد وظایف یک پروژه |

نمونه خروجی `__str__`:
```
Task ID : 101
Title   : Study Python
Priority: 4
Status  : Pending
```

---

## 📊 محاسبه درصد پیشرفت پروژه

```
Progress = (Completed Tasks / Total Tasks) × 100
```

مثال: `Total = 10, Completed = 7 → Progress = 70%`

---

## ✅ امکانات برنامه

- افزودن / ویرایش / حذف / نمایش پروژه‌ها
- افزودن / ویرایش / حذف / جستجوی وظایف
- نمایش وظایف یک پروژه یا همه وظایف
- تغییر وضعیت وظیفه
- نمایش وظایف انجام‌شده و انجام‌نشده
- مرتب‌سازی وظایف
- نمایش آمار (تعداد کل، تعداد هر پروژه)
- محاسبه درصد پیشرفت پروژه
- نمایش امتیاز وظایف

---

## 📏 قوانین پروژه

- شناسه پروژه و شناسه وظیفه نباید تکراری باشند
- عنوان وظیفه و نام پروژه نباید خالی باشند
- اولویت باید بین 1 تا 5 باشد
- وضعیت فقط می‌تواند `Pending` یا `Completed` باشد
- وظایف فوری (`UrgentTask`) فقط می‌توانند اولویت 4 یا 5 داشته باشند

---

## 🧠 مفاهیم شیءگرایی استفاده‌شده

✅ طراحی کلاس &nbsp;&nbsp; ✅ طراحی ماژولار &nbsp;&nbsp; ✅ Encapsulation
✅ Inheritance &nbsp;&nbsp; ✅ Polymorphism &nbsp;&nbsp; ✅ Exception Handling &nbsp;&nbsp; ✅ Dunder Methods

---

**[Miss Zero]**
GitHub: [github.com/Zero-miss-0](https://github.com/Zero-miss-0)
