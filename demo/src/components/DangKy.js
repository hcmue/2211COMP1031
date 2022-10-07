import { useForm } from "react-hook-form";

export const DangKy = () => {
    const { register, handleSubmit, watch, formState: { errors } } = useForm();
    const onSubmit = (data) => {
        console.log(data);
    }
    console.log(watch("username"))

    return (
        <div>
            <form onSubmit={handleSubmit(onSubmit)}>
                Username: <input {...register("username")} />
                <br />
                Password:
                <input type="password" {...register("exampleRequired", { required: true })} />
                {errors.exampleRequired && <span>This field is required</span>}
                <br />
                <input type="submit" value="Register" />
            </form>
        </div>
    )
}