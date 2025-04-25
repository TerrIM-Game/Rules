
Папка **system** создана для настройки инструментария сообщества
Пожалуйста не меняйте ее, если глубоко не понимаете что делаете. 


В разделе [Инструменты](Ω_system/tools/README.md) находящемся в папке **system/tools/** описаны программы которыми мы пользуемся.
* [Obsidian](Ω_system/tools/Obsidian.md)
* [Git](Ω_system/tools/Git.md)
* [GitHub](Ω_system/tools/GitHub.md)


# Обсидиан

Программа [Obsidian](Ω_system/tools/Obsidian.md) это записная книжка обладающая рядом свойств необходимых нашему сообществу. Она упрощает редактирование документации размещенной на [GitHub](Ω_system/tools/GitHub.md)

## Свойства

В разделе system/templates/ размещены шаблоны свойств для [Obsidian](Ω_system/tools/Obsidian.md) которые позволяют вставлять типовые наборы свойств в разные типы заметок: 
* [project](Ω_system/templates/project.md)
* [member](Ω_system/templates/member.md)
* [contract](Ω_system/templates/contract.md)

Свойства вставляемые шаблонами позволят автоматизировать обработку документации.

В разделе system/types/ размещены типы документов для [Obsidian](Ω_system/tools/Obsidian.md) тип документа надо заполнять в свойство типового документа для автоматизации. Зная тип документа в файле наши боты смогут знать какие свойства надо из него считать. 
Например: 
* [Договор](Ω_system/types/Contract.md)
* [Проект](Ω_system/types/Project.md)
* [Участник](Ω_system/types/Member.md)
