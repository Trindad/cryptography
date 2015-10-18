	.file	"programa.c"
	.local	mesg
	.comm	mesg,100,32
	.local	response
	.comm	response,100,32
	.comm	pointer_to_function,4,4
	.section	.rodata
.LC0:
	.string	"Voce enviou: %s\n"
	.text
	.globl	one_function
	.type	one_function, @function
one_function:
.LFB0:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$24, %esp
	movl	$mesg, 8(%esp)
	movl	$.LC0, 4(%esp)
	movl	$response, (%esp)
	call	sprintf
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE0:
	.size	one_function, .-one_function
	.globl	other_function
	.type	other_function, @function
other_function:
.LFB1:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	movl	$1634885968, response
	movl	$1936614754, response+4
	movl	$1870012460, response+8
	movl	$1663067491, response+12
	movl	$1818455663, response+16
	movl	$544565621, response+20
	movl	$1920213103, response+24
	movl	$1818321505, response+28
	movl	$555839336, response+32
	movw	$33, response+36
	popl	%ebp
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE1:
	.size	other_function, .-other_function
	.section	.rodata
.LC1:
	.string	">>%s<<\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB2:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$80, %esp
	movl	$one_function, pointer_to_function
	movl	$0, 8(%esp)
	movl	$2, 4(%esp)
	movl	$2, (%esp)
	call	socket
	movl	%eax, 76(%esp)
	movl	$16, 4(%esp)
	leal	56(%esp), %eax
	movl	%eax, (%esp)
	call	bzero
	movw	$2, 56(%esp)
	movl	$0, (%esp)
	call	htonl
	movl	%eax, 60(%esp)
	movl	$32000, (%esp)
	call	htons
	movw	%ax, 58(%esp)
	movl	$16, 8(%esp)
	leal	56(%esp), %eax
	movl	%eax, 4(%esp)
	movl	76(%esp), %eax
	movl	%eax, (%esp)
	call	bind
.L4:
	movl	$16, 36(%esp)
	leal	36(%esp), %eax
	movl	%eax, 20(%esp)
	leal	40(%esp), %eax
	movl	%eax, 16(%esp)
	movl	$0, 12(%esp)
	movl	$1000, 8(%esp)
	movl	$mesg, 4(%esp)
	movl	76(%esp), %eax
	movl	%eax, (%esp)
	call	recvfrom
	movl	%eax, 72(%esp)
	movl	72(%esp), %eax
	addl	$mesg, %eax
	movb	$0, (%eax)
	movl	$mesg, 4(%esp)
	movl	$.LC1, (%esp)
	call	printf
	movl	pointer_to_function, %eax
	call	*%eax
	movl	$response, (%esp)
	call	strlen
	movl	%eax, 72(%esp)
	movl	72(%esp), %eax
	movl	$16, 20(%esp)
	leal	40(%esp), %edx
	movl	%edx, 16(%esp)
	movl	$0, 12(%esp)
	movl	%eax, 8(%esp)
	movl	$response, 4(%esp)
	movl	76(%esp), %eax
	movl	%eax, (%esp)
	call	sendto
	jmp	.L4
	.cfi_endproc
.LFE2:
	.size	main, .-main
	.ident	"GCC: (Debian 4.7.2-5) 4.7.2"
	.section	.note.GNU-stack,"",@progbits
